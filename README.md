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

![missing](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/f6012d97-24d1-463a-8e18-bc3d64f2eb3e)

**Bar plot** presents percentage values for each type of the participancy in the data community. 
![activity_type](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/6082143c-b323-469f-9de3-e138c00970c0)

**Boxplots** represent range of surveyees' abilities
![boxplots](https://github.com/cropsini2137/ProjektAnalitiks/assets/159359001/c1c682ae-c321-4a64-b8ab-9a396ca5c42f)

**Combo plots** display the same data with simpler visualization
![histogramsy](https://github.com/cropsini2137/ProjektAnalitiks/assets/159359001/23225e00-3d29-463c-a2cb-d8008c6c0a56)

**Correlation plot** visualizes similarity between data. Groups of similar skills have been highlighted and top-right corner with repeating values has been removed for clarity.
![skill_heatmap](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/b169000e-8d07-44f8-bf53-d8d5b16161f7)

**Elbow method** shows the optimal k value for clustering, which is essential to know before plotting a dendrogram. In this case both k=3 and k=4 are fine, but we decided to go with k=4.
![elbow_method](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/5d792b5c-34ee-467f-af20-a549f45e7c25)

**Dendrogram** images the hierarchical clustering of various data competencies. We can easily observe a split into hard skills and soft skills.
![tree](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/23ab7ae2-80b5-4796-ad4d-1f9c84aa73ca)

**Stacked column plot** represents distribution of respondents' skills. It is sorted descendingly based on a sum of 3.0 and 4.0 responses to reveal which skills are the most often.
![stacked_column_plot](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/8c7cf56c-d03d-4eca-a131-1319a806f4b6)

The plot below represents top 15 skills, including only responses from 2 to 4.
![top_skills_column_lot](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/0949458c-dff2-4cfe-b08a-c1dc7ddc9fb3)

**PCA analysis** groups data into categories. 
![pca_analysis](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/84e56001-eb8b-439a-bf28-471b54a109f9)

**Violin plots** illustrate the distribution of proficiency levels across different clusters for various competencies. Each plot combines a box plot and a density plot, showing the range, median, and distribution shape of proficiency scores within each cluster.
![violin_plots](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/39038887-673e-417e-bb16-c47ebac27044)

**Heatmap** represents the surveyees' abilities. This visualization was splitted in the project into smaller skill groups to improve the readability. This approach helps in noticing which respondents are confident in their skills in respective skill groups.
![respondents_skills_heatmap](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/0de2f311-fbcd-47a1-b1aa-be10dbdc129f)

**Grouping tool** is used to group surveyees in the optimal way using the parameters selected by a user. Below there is an example of such grouping.
![image](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/e27b87fd-2d8c-47e4-8d01-3ec12c1aa329)

![image](https://github.com/cropsini2137/ProjektAnalitiks/assets/52826998/461393a5-8fc2-47b6-84ac-b7cc480018ec)

### Project summary 📋

**Data cleaning** part has made significant changes to the dataset, leaving only rows and columns with non-missing values to ensure quality presentation of data on further stages. This process also helped with uncluttering visualisations that were made on later stages.

In chapter "**Exploratory Data Analysis**" we performed a series of basic data exploration and visualization techniques. After each analysis there is a visualization and simple summary to present insights that were collected.

**Advanced EDA** section covered some advanced techniques for data exploration and visualisation, such as: **heatmap** (for visualising correlation and missing values), simple **bar charts** and **column charts**, **box-plots**, **scatter plots**, **violin plots**, **stacked column plots**, **line plots** or **dendrogram**. 

It also covered some basic forms of scientific approach to data in forms of: **clustering**, **outlier detection**, **data imputation**, **PCA** and **regression analysis**.

### License 🧾

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.
