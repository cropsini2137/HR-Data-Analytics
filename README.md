# HR Data Analytics
team rzulci vabank 🟨

![DALL·E 2024-05-31 00 03 16 - A vibrant logo featuring a wealthy culturist pope  The pope should have a muscular build similar to a bodybuilder, wearing traditional papal attire wi](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/ea3a6ee4-3bdd-4100-afdd-f68bfa2f386f)

![](https://komarev.com/ghpvc/?username=prod-rejent&style=flat-square&color=yellow&label=View+count)

## Project contents

- [HR Data Analytics](#hr-data-analytics)
  - [Project contents](#project-contents)
  - [Team members 👥](#team-members-)
  - [Project overview](#project-overview)
    - [General description 📙](#general-description-)
    - [Objectives 🎯](#objectives-)
    - [Requirements and methodology 📚](#requirements-and-methodology-)
    - [Requirements ⚙️](#requirements-️)
      - [Descriptive statistics 📝](#descriptive-statistics-)
      - [Correlation analysis \*️⃣](#correlation-analysis-️⃣)
      - [Clustering analysis ✨](#clustering-analysis-)
      - [HR Benefits 👥](#hr-benefits-)
    - [Conclusions and visualizations 📊](#conclusions-and-visualizations-)
    - [Project summary 📋](#project-summary-)
    - [License 🧾](#license-)

## Team members 👥
★ Ryan Jabłoński
✰ Maciej Mądrzyk
✰ Mikołaj Stojek

## Project overview

### General description 📙

This project is focused on analyzing HR data collected during a survey about its respondents skills, shared within the context of **Wrocław AI Team** - an initiative designed to facilitate the execution of *AI, Data Science, and Business Intelligence (BI)* projects. The primary goal of this project is to create a practical learning opportunity, where individuals with shared interests collaborate and learn from each other.

This project data is stored within folders:
- Folder **data** stores raw data files in .csv form used on different stages of analysis,
- In **notebooks** folder there are separate notebooks for each stage of analysis.

The dataset size after cleaning is 37 columns, 59 rows. It contains survey responses from individuals (those willing to actively participate in community) about their skills and competencies. It includes columns that can be further grouped into categories as such:
- `ID` - unique identifier for each entry,
- `W jaki sposób chcesz uczestniczyć w Community?` - response on how the participant wants to engage in the community,
Skillset columns include five types of values, ranging from 0.0 to 4.0. :
- `Programming: Python, R, Bash, CLI`,
- `Data Science: ML / NLP / AI`,
- `Cloud platforms: AWS / Azure / GCP`,
- `Databases: SQL / NoSQL`,
- `BI tools`,
- `Soft skills`,
- `Domain expertise` (e.g., FinTech, HealthTech, FashionTech, etc.)

---
### Objectives 🎯

The main objective is aimed at improving team management by utilizing data on the declared skills and competencies of individuals willing to participate in projects related to *Data Science / BI / Data Analytics* topics. By analyzing survey responses and clustering respondents based on their skills, the project aims to provide valuable insights that will help project founders form effective teams. In short, this analysis focuses on creating the strongest groups, with the adjustable group creator implemented at the end of the notebook **03_Advanced_EDA**.

It also focuses on enhancing team management by leveraging data on declared skills and competencies of individuals eager to participate in AI, Data Science, and Business Intelligence (BI) projects. By analyzing survey responses and clustering respondents based on their skills, we aim to provide valuable insights that assist project founders in forming effective teams.

A significant objective is to develop participants' skills in using tools such as GitHub, VS Code, and programming in Python. Additionally, the project aims to teach essential Data Science skills.

### Requirements and methodology 📚

To achieve the project's objectives, we will employ various data analysis and clustering techniques, which are essential in extracting valuable insights from the dataset. We will start with exploratory data analysis, including descriptive statistics and visualisation techniques.
Later on we'll employ clustering algorithms to determine the most appropriate method for segmenting the dataset.

### Requirements ⚙️
You can find the requirements.txt file attached in the main repository folder. There are the essential libraries needed to launch the notebook's content.

This project requires strict adherence to the directory and file structure for the program to read and write data correctly. Any changes to the directory structure may prevent the code from functioning properly.

### Folder structure

```markdown
📂 ProjektAnalitiks/
├── 📂 data/
│   ├── 📂 01_Raw/
│   │   └── 📄 01_DataCompetencySurvey.csv
│   ├── 📂 02_Interim/
│   │   ├── 📄 cleaned_data.csv
│   │   ├── 📄 cleaned_dataset.csv
│   │   ├── 📄 cleaned.csv
│   │   ├── 📄 dropped_rows_columns_imputed.csv
│   │   ├── 📄 dropped_rows_columns.csv
│   │   └── 📄 rows_with_most_missing_values.csv
│   └── 📂 03_Processed/
│       ├── 📄 cleaned_data.csv
│       └── 📄 data_cleaned.csv
├── 📂 docs/
├── 📂 figures/
├── 📂 models/
├── 📂 notebooks/
│   ├── 📂 .ipynb_checkpoints/
│   └── 📂 steps/
│       ├── 📄 01_Data_Cleaning.ipynb
│       ├── 📄 02_Exploratory_Data_Analysis.ipynb
│       ├── 📄 03_Advanced_EDA.ipynb
│       └── 📄 04_Grouping.ipynb
│   ├── 📄 01_Data_Preprocessing.ipynb
│   └── 📄 02_EDA_and_Grouping.ipynb
├── 📄 .gitkeep
├── 📄 .gitignore
└── 📄 README.md
```

As a part of analysis, we want to check or implement such parts like:

#### Descriptive statistics 📝

**Summary statistics** - Calculating basic statistics for each skill category to understand the overall distribution of skills.

**Frequency distribution** - Determine the frequency of each skill level across all respondents to identify the most common skill levels.
#### Correlation analysis *️⃣

**Skill correlation** - Analyze the correlation between different skills to identify patterns and relationships.

#### Clustering analysis ✨
**k-means clustering** - Grouping respondents into clusters based on their skill sets helped to identify distinct profiles / archetypes within the data.

**Hierarchical clustering** - hierarchical clustering was used to visualize how respondents can be grouped based on skill similarities.

Other scientific techniques used in this project are **DB-SCAN**, **Regression modelling**, **Data imputation**, and **PCA analysis**.

#### HR Benefits 👥

This approach is not only beneficial for team formation but also offers advantages for Human Resources (HR) departments. It provides a data-driven method to understand the skill distribution within the organization, improving recruitment processes, talent management, and personal development strategies.

By identifying distinct groups within the community, the project aims to improve decision-making in team formation, ensuring that each team has the right mix of skills and competencies to tackle real-world business challenges.

### Conclusions and visualizations 📊

**[This heatmap](notebooks/01_Data_Preprocessing.ipynb#heatmap)** visualizes **missing values** in the original dataset. There are significant portions of missing values across several columns/rows, with some having more gaps than the others. We dealt with them by removing rows and columns with over 25% data missing after carefully analyzing the heatmap, consequences of such act and for ease of cleaning process. The data with missing values would be irrelevant in context of our analysis. Deleted rows and columns would not bring any positive impact on the accuracy of further outcomes, due to their emptiness. We could observe such data characteristics:

**In columns**: not all are useful enough for analysis and some are very empty. 

**In rows**: because of incomplete surveys - they would skew results of the analysis. 

**![missing](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/fd406a5b-2eb0-4846-b7d7-b7ba3ead8368)**

**[Bar plot](https://github.com/cropsini2137/ProjektAnalitiks/blob/main/notebooks/02_EDA_and_Grouping.ipynb#L5)**
presents percentage values for each type of the participancy in the data community. 

![image](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/0fa33a7b-23ef-462f-9d88-65f07b33a6f1)

**[Correlation plot](https://github.com/cropsini2137/ProjektAnalitiks/blob/main/notebooks/02_EDA_and_Grouping.ipynb#L6)**
visualizes similarity between data. Groups of similar skills have been highlighted and top-right corner with repeating values has been removed for clarity.

![skill_heatmap](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/d538d343-f1c5-4dcf-b47f-194703d4bc96)

**[Elbow method](https://github.com/cropsini2137/ProjektAnalitiks/blob/main/notebooks/02_EDA_and_Grouping.ipynb#L7)**
shows the optimal k value for clustering, which is essential to know before plotting a dendrogram. In this case both k=3 and k=4 are fine, but we decided to go with k=4.

![elbow_method](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/0f24c206-eac3-4b73-854c-a98d40bd3f6f)

**[Dendrogram](https://github.com/cropsini2137/ProjektAnalitiks/blob/main/notebooks/02_EDA_and_Grouping.ipynb#L8)**
images the hierarchical clustering of various data competencies. We can easily observe a split into hard skills and soft skills.

![tree](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/f3609c5e-cda6-4554-abb4-d96b86894dca)

**[Stacked column plot](https://github.com/cropsini2137/ProjektAnalitiks/blob/main/notebooks/02_EDA_and_Grouping.ipynb#L9)**
represents distribution of respondents' skills. It is sorted descendingly based on a sum of 3.0 and 4.0 responses to reveal which skills are the most often.

![stacked_column_plot](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/d3955537-007f-4e5b-999c-9e2bd4340499)

**[Heatmap](https://github.com/cropsini2137/ProjektAnalitiks/blob/main/notebooks/02_EDA_and_Grouping.ipynb#L11)**
represents the surveyees' abilities. This visualization was splitted in the project into smaller skill groups to improve the readability. This approach helps in noticing which respondents are confident in their skills in respective skill groups.

![respondents_skills_heatmap](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/0de2f311-fbcd-47a1-b1aa-be10dbdc129f)

**[Grouping tool](https://github.com/cropsini2137/ProjektAnalitiks/blob/main/notebooks/02_EDA_and_Grouping.ipynb#L11)**
is used to group surveyees in the optimal way using the parameters selected by a user. This process can be utilized to generate different propositions on what members to choose into a specific project. Below there is an example of such grouping.

![image](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/e717d9e5-0bf5-41ba-8da7-a3d178b4b129)

**Grouping example** - Best technically skilled group of 4

**Selection**: Select "Technical skills"

**Sliders**: Min. group size -> 4, Max. group size -> 4, Min. 4.0 answers -> 2, Min. threshold > Not aware, Max. generated groups > 1

**Clustering**: Agglomerative, Metric -> euclidean, Linkage -> Linear, Distance threshold -> 1.50 

![image](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/01e4c7c1-dd7a-4a99-8f87-78546f70b9da)

Users can select various IT skills across categories such as Cloud & Databases, Business Intelligence, Programming, Data Science, Industry Knowledge and Soft skills.

Multiple clustering algorithms are available, including **Agglomerative, K-means, and DB-SCAN**.

Users can choose the metric (f.e., Euclidean) and linkage criteria (f.e., single) for the **agglomerative** clustering process.

In case of **k-means** clustering, users can set up random state (default is 42) and number of clusters from 1 to 10.

For **DB-SCAN**, it is possible to change DBSCAN eps and mininum number of samples. 

**eps** metric is the maximum distance between two samples for one to be considered as in the neighborhood of the other. 

min_samples is the number of samples (or total weight) in a neighborhood for a point to be considered as a core point. This includes the point itself. If min_samples is set to a higher value, DBSCAN will find denser clusters, whereas if it is set to a lower value, the found clusters will be more sparse.

### Project summary 📋

**Data cleaning** part has made significant changes to the dataset, leaving only rows and columns with non-missing values to ensure quality presentation of data on further stages. This process also helped with uncluttering visualisations that were made on later stages.

In chapter **Exploratory Data Analysis** 

**Advanced EDA** section covered some advanced techniques for data exploration and visualisation, such as: **heatmap** (for visualising correlation and missing values), **bar charts** and **column charts**, **box-plots**, **scatter plots**, **violin plots**, **stacked column plots**, **line plots** and **dendrogram**. We performed a series of basic data exploration and visualization techniques. After each analysis there is a visualization and simple summary to present insights that were collected.

It also covered some basic forms of scientific approach to data in forms of: **clustering**, **outlier detection**, **data imputation**, and **regression analysis**.

Lastly, in notebook **04_Grouping** there is a grouping tool. 
This methodology not only enhances collaborative efficiency but also maximizes the potential for collective learning and development within each group.
Tailored for educational and professional purposes, this application stands as a solution for skill-based group formation.

### License 🧾

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.
