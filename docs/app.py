from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import AgglomerativeClustering, KMeans, DBSCAN
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Patch
import os

app = Flask(__name__, template_folder='.')

# Load the dataset
data = pd.read_csv(r'C:\Users\rejen\OneDrive\Documents\GitHub\ProjektAnalitiks\data\03_Processed\cleaned_data.csv')

# Define the updated categories with original names for columns
categories_updated = {
    'Cloud & Databases': ['Cloud: AWS', 'Cloud: Azure', 'Cloud: GPC', 'Databases: NoSQL', 'Databases: SQL'],
    'Business Intelligence (BI)': ['BI: PowerBI', 'BI: Tableau'],
    'Programming': ['Programming: R', 'Programming: Python', 'Programming: Bash', 'CLI: (np. Bash, PowerShell, CMD)', 'Version Control: GIT', 'Containers: Docker', 'Front End: (HTML, JavaScript, CSS)'],
    'Data Science': ['Area: Time Series', 'Area: Classical ML (Clustering, Regression, Classification)', 'Area: NLP', 'Area: Computer Vision'],
    'Industry knowledge': ['FinTech', 'HealthTech', 'FashionTech', 'E-commerce', 'SportTech', 'Non-profit', 'PropTech (nieruchomości)', 'Cybersecurity', 'HR'],
    'Soft skills': ['Project Management','Promocja w Social Media','Ux/Ui','Projektowanie graficzne','Nawiązywanie Relacji z Biznesem','Nawiązywanie Relacji z naukowcami','Pozyskiwanie finansowania','Współpraca z administracją UEW']
}

def process_category(category_name, columns, min_group_size, max_group_size, min_4_0_answers, min_threshold, clustering_option, max_generated_groups, n_clusters=None, metric='euclidean', linkage='average', distance_threshold=1.5):
    try:
        competencies_data = data[columns]

        # Filter competencies based on the minimum threshold
        filtered_data = competencies_data.apply(lambda col: col.map(lambda x: x if x >= min_threshold else np.nan)).dropna(how='all', axis=1)

        # Normalize the data
        scaler = StandardScaler()
        competencies_scaled = scaler.fit_transform(filtered_data.fillna(0))

        # Calculate similarity matrix
        similarity_matrix = cosine_similarity(competencies_scaled)

        # Perform clustering
        if clustering_option == 'Agglomerative':
            clustering = AgglomerativeClustering(n_clusters=n_clusters, metric=metric, linkage=linkage, distance_threshold=distance_threshold)
        elif clustering_option == 'K-means':
            clustering = KMeans(n_clusters=n_clusters)
        elif clustering_option == 'DB-SCAN':
            clustering = DBSCAN(eps=0.5, min_samples=min_group_size)

        clustering.fit(similarity_matrix if clustering_option != 'K-means' else competencies_scaled)

        # Assign groups based on clustering
        data['Group'] = clustering.labels_

        # Filter out groups with less than min_group_size people
        group_sizes = data['Group'].value_counts()
        valid_groups = group_sizes[group_sizes >= min_group_size].index
        data_valid = data[data['Group'].isin(valid_groups)]

        # Split larger groups into smaller ones if necessary, ensuring each group has at least min_4_0_answers 4.0 values
        new_groups = []
        for group in valid_groups:
            group_data = data_valid[data_valid['Group'] == group]
            group_size = len(group_data)
            while group_size > max_group_size:
                high_competency = (group_data[columns] == 4.0).sum(axis=1)
                if high_competency.sum() == 0:
                    break

                high_comp_individuals = group_data[high_competency >= min_4_0_answers]
                remaining_individuals = group_data[high_competency < min_4_0_answers]

                if len(high_comp_individuals) >= max_group_size:
                    new_groups.append(high_comp_individuals.iloc[:max_group_size])
                    group_data = group_data.iloc[max_group_size:]
                else:
                    split_group = pd.concat([high_comp_individuals, remaining_individuals.iloc[:max_group_size - len(high_comp_individuals)]])
                    new_groups.append(split_group)
                    group_data = remaining_individuals.iloc[max_group_size - len(high_comp_individuals):]

                group_size = len(group_data)

            if group_size >= min_group_size and (group_data[columns] == 4.0).sum().sum() >= min_4_0_answers:
                new_groups.append(group_data)

        if not new_groups:
            return "No groups meet the specified criteria."

        # Plot heatmaps for each new group, showing only the best skills
        group_counter = 1
        for group_data in new_groups:
            if group_counter > max_generated_groups:
                break
            group_ids = group_data['ID']
            group_competencies = group_data[columns]

            # Filter competencies to only include those rated according to the minimum threshold
            best_competencies = group_competencies.apply(lambda col: col.map(lambda x: x if x >= min_threshold else np.nan))
            best_competencies = best_competencies.dropna(how='all').dropna(axis=1, how='all')

            if (best_competencies == 4.0).sum().sum() < min_4_0_answers:
                continue

            sorted_competencies = best_competencies.apply(lambda col: col.sort_values(ascending=False), axis=0)

            if not sorted_competencies.empty:
                heatmap_data_renamed = sorted_competencies.set_index(group_ids)
                group_id_list = ', '.join(map(str, group_ids))

                plt.figure(figsize=(14, 8))
                sns.heatmap(heatmap_data_renamed.T, cmap='YlGnBu', cbar=False, annot=False, fmt=".1f", linewidths=.5, vmin=2, vmax=4)
                plt.title(f'ID: {group_id_list} - group {group_counter} - top competencies', fontsize=20)
                plt.xticks(fontsize=8)
                plt.yticks(fontsize=8)
                plt.xlabel('ID', fontsize=15)
                plt.ylabel('Competencies', fontsize=15)
                legend_patches_custom = [
                    Patch(color=sns.color_palette("YlGnBu", 3)[0], label='2.0 - Interested'),
                    Patch(color=sns.color_palette("YlGnBu", 3)[1], label='3.0 - Competent'),
                    Patch(color=sns.color_palette("YlGnBu", 3)[2], label='4.0 - Expert')
                ]
                plt.legend(handles=legend_patches_custom, loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')
                heatmap_filename = f'static/heatmap_{group_counter}.png'
                plt.savefig(heatmap_filename)
                plt.close()
                group_counter += 1

        return "Heatmaps generated successfully."

    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html', categories=categories_updated)

@app.route('/process', methods=['POST'])
def process():
    form_data = request.form
    selected_skills = form_data.getlist('skills')
    min_group_size = int(form_data['min_group_size'])
    max_group_size = int(form_data['max_group_size'])
    min_4_0_answers = int(form_data['min_4_0_answers'])
    min_threshold = float(form_data['min_threshold'])
    clustering_option = form_data['clustering_option']
    max_generated_groups = int(form_data['max_generated_groups'])
    n_clusters = int(form_data['n_clusters']) if 'n_clusters' in form_data else None
    metric = form_data['metric']
    linkage = form_data['linkage']
    distance_threshold = float(form_data['distance_threshold'])

    result = process_category('Custom selection', selected_skills, min_group_size, max_group_size, min_4_0_answers, min_threshold, clustering_option, max_generated_groups, n_clusters=n_clusters, metric=metric, linkage=linkage, distance_threshold=distance_threshold)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)