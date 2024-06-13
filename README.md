# HR Data Analytics
team rzulci vabank 🟨

![DALL·E 2024-05-31 00 03 16 - A vibrant logo featuring a wealthy culturist pope  The pope should have a muscular build similar to a bodybuilder, wearing traditional papal attire wi](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/ea3a6ee4-3bdd-4100-afdd-f68bfa2f386f)

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

To achieve the project's objectives, we will employ various data analysis and clustering techniques, which are essential in extracting valuable insights from the dataset.
We will start with exploratory data analysis, including descriptive statistics and visualisation techniques.

We'll employ clustering algorithms to determine the most appropriate method for segmenting the dataset.

In order to achieve desired insights from the data provided, we decided to use:
- **Python 🐍** as the primary programming language for data analysis and clustering,
- **Pandas 🐼🐼** - for data manipulation and analysis,
- **NumPy 🔢** - for numerical operations,
- **Matplotlib and Seaborn 📈📊** - for data visualization,
- **Scikit-learn & Scipy 🔬** - for implementing clustering algorithms and evaluation metrics,
- **VS Code & Git 👨🏻‍💻** - code development and version control integration.

### Requirements ⚙️
You can find the requirements.txt file attached in the main repository folder. Here are the essential libraries needed to launch the notebook's content:

ipywidgets
ipython
matplotlib==3.6.3
numpy==1.24.0
pandas==1.5.3
seaborn==0.11.2
scipy==1.9.3
scikit-learn==1.1.3

As a part of analysis, we want to check or implement such parts like:

#### Descriptive statistics 📝

**Summary statistics** - Calculating basic statistics for each skill category to understand the overall distribution of skills.

**Frequency distribution** - Determine the frequency of each skill level across all respondents to identify the most common skill levels.
#### Correlation analysis *️⃣

**Skill correlation** - Analyze the correlation between different skills to identify patterns and relationships.

#### Clustering analysis ✨
**k-means clustering** - Grouping respondents into clusters based on their skill sets helped to identify distinct profiles / archetypes within the data.

**Hierarchical clustering** - hierarchical clustering was used to visualize how respondents can be grouped based on skill similarities.

Other scientific techniques used in this project are **Regression modelling**, **Data imputation**, and **PCA analysis**.

#### HR Benefits 👥

This approach is not only beneficial for team formation but also offers advantages for Human Resources (HR) departments. It provides a data-driven method to understand the skill distribution within the organization, improving recruitment processes, talent management, and personal development strategies.

By identifying distinct groups within the community, the project aims to improve decision-making in team formation, ensuring that each team has the right mix of skills and competencies to tackle real-world business challenges.

### Conclusions and visualizations 📊

This heatmap visualizes **missing values** in the original dataset. There are significant portions of missing values across several columns/rows, with some having more gaps than the others. We dealt with them by removing rows and columns with over 25% data missing after carefully analyzing the heatmap, consequences of such act and for ease of cleaning process. The data with missing values would be irrelevant in context of our analysis. Deleted rows and columns would not bring any positive impact on the accuracy of further outcomes, due to their emptiness. We could observe such data characteristics:
In columns: not all are useful enough for analysis and some are very empty. 
In rows: because of incomplete surveys - they would skew results of the analysis. 

![missing](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/1dcaf219-fa28-47a4-9f9a-4d5afb3c74b3)

**Bar plot** presents percentage values for each type of the participancy in the data community. 
![activity_type](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/15358707-bf3b-46c7-bfbc-ea5ae0486d9d)

**Boxplots** represent range of surveyees' abilities
![boxplots](https://github.com/cropsini2137/ProjektAnalitiks/assets/159359001/c1c682ae-c321-4a64-b8ab-9a396ca5c42f)

**Combo plots** display the same data with simpler visualization
![histogramsy](https://github.com/cropsini2137/ProjektAnalitiks/assets/159359001/23225e00-3d29-463c-a2cb-d8008c6c0a56)

**Correlation plot** visualizes similarity between data. Groups of similar skills have been highlighted and top-right corner with repeating values has been removed for clarity.
![skill_heatmap](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/e4760483-7bd9-4678-a6f0-736f3d861664)

**Elbow method** shows the optimal k value for clustering, essential before plotting a dendrogram.
![elbow_method](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/22fc5561-3bf2-4abb-b554-f2850bfe41df)

**Dendrogram** images the hierarchical clustering of various data competencies. 
![drzewogram](https://github.com/cropsini2137/ProjektAnalitiks/assets/159359001/60b6d45a-7296-4bde-8b70-edff4f4d4c48)

**Stacked column plot** represents distribution of respondents' skills. It is sorted descendingly based on a sum of 3.0 and 4.0 responses.
![stacked_column_plot](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/f8524e05-adb9-4699-8344-fedb66e76614)

The plot below represents top 15 skills, including only responses from 2 to 4.
![top_skills_column_lot](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/dc5f012f-eda8-4965-89ff-76e0ccecaf37)

**Word cloud** clusters skills of surveyees and visually aid to differentiate the most popular ones from the least popular ones.
![wordcloud](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/33fcb9a5-3f2e-47ae-a802-be66da8da34e)

**PCA analysis** groups data into categories.
![klasta](https://github.com/cropsini2137/ProjektAnalitiks/assets/159359001/87c9b8b3-06ba-4c37-a0c2-47b302fb461d)

**Violin plots** illustrate the distribution of proficiency levels across different clusters for various competencies. Each plot combines a box plot and a density plot, showing the range, median, and distribution shape of proficiency scores within each cluster.
![violin_plots](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/b3ce5dad-f0e0-4993-818c-947774fee18e)

**Heatmap** represents the data and surveyees' abilities.
![respondents_skills_heatmap](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/f648ae39-e20a-42e5-b5d1-e2794de5ac81)

**Grouping tool** is used to sort surveyees in the optimal way using the parameters selected by a user.

### Project summary 📋

**Data cleaning** part has made significant changes to the dataset, leaving only rows and columns with non-missing values to ensure quality presentation of data on further stages. This process also helped with uncluttering visualisations that were made on later stages.

In chapter "**Exploratory Data Analysis**" we performed a series of basic data exploration and visualization techniques. After each analysis there is a visualization and simple summary to present insights that were collected.

**Advanced EDA** section covered some advanced techniques for data exploration and visualisation, such as: **heatmap** (for visualising correlation and missing values), simple **bar charts** and **column charts**, **box-plots**, **scatter plots**, **violin plots**, **stacked column plots**, **line plots** or **dendrogram**. 

It also covered some basic forms of scientific approach to data in forms of: **clustering**, **outlier detection**, **data imputation**, **PCA** and **regression analysis**.

### License 🧾

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.
