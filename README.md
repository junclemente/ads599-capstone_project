# 🚀 California School-Level Early Warning System (EWS) for Predicting Graduation Outcomes

This project is a part of the ADS-599 course in the Applied Data Science Program at the University of San Diego.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

-- **Project Status: Planned**

# Installation

To use this project, first clone the repo on your device using the command below:

```bash
git init
git clone https://github.com/junclemente/msads_capstone.git
```

## Environment Setup

This project uses a conda environment specified in a YAML file for
reproducibility and consistent development. Ensure you have
[Anaconda](https://www.anaconda.com/download) or
[Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main)
installed.

**Create the Environment**
Run the following:

```bash
conda env create -f environment.yml
```

**Update the Environment (if needed)**
If there are any updates to the environment, you can update the environment with the following:

```bash
conda env update -f environment.yml --prune
```

The `--prune` option cleans the environment by removing packages that are no longer required.

# Project Intro / Objective

The main purpose of this project is to develop a school-level Early Warning System (EWS) that identifies California public high schools at risk of low graduation outcomes using only public, non-PII datasets. By leveraging statewide indicators aligned with the ABC framework—Attendance, Behavior, and Course performance—this project demonstrates that actionable early-warning signals can be generated without relying on restricted student-level records.

The goal is to provide California educators, policymakers, and district leaders with a scalable, transparent, and privacy-preserving tool for monitoring emerging risk, understanding systemic inequities, and supporting data-informed planning and resource allocation.

# Partner(s)/Contributor(s)

- [Amayrani Balbuena](https://github.com/amayranib)
- [Jun Clemente](https://github.com/junclemente)
- [Tanya Ortega](https://github.com/tanyaort)

# Methods Used

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Predictive Modeling and Machine Learning Classification
- Feature Selection using Random Forest
- Data Visualization

# Technologies

- Python
- Pandas 
- Numpy 
- Matplotlib, Seaborn
- Jupyter Notebook / VSCode
- Streamlit
- Conda
- Git / Github

# Project Description

This project develops a simplified Early Warning System (EWS) that predicts high-school graduation outcomes using only publicly accessible datasets from the California Department of Education (CDE). Using 2021–22 school-level indicators—such as graduation rates, chronic absenteeism, FRPM eligibility, teacher experience, and school characteristics—combined with county-level climate data, we built a cleaned modeling dataset of 958 schools and 25 predictors. A binary target (“At Risk” < 90% graduation rate) highlighted a 26.3% minority class, and analysis confirmed strong ABC-aligned patterns between absenteeism, socioeconomic disadvantage, teacher experience, and graduation outcomes. Multiple machine learning models were evaluated with PR-AUC, Precision, Recall, and F1 due to class imbalance; Random Forest and Logistic Regression performed best, with top predictors including chronic absenteeism, unexcused absences, FRPM eligibility, still-enrolled rate, and A–G completion rate. Key challenges included inconsistent county reporting, FERPA-related suppression, and missing climate indicators, though all data were aggregate and fully public.

# License

This project is licensed under the [MIT License](./LICENSE).

# Acknowledgments

You can mention and thank those who technically helped you during the project.

# 🤖 AI Assistance Disclosure 

Parts of this project were developed with the help from ChatGPT (OpenAI):
- Debugging Python functions and pipeline logic
- Drafting / rewriting docstrings and short notebook summaries 
- Creating small code snippets

All generated code and text were reviewed and edited by the authors. 
