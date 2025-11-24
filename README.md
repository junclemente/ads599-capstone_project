# Project Title

This project is a part of the ADS-599 course in the Applied Data Science Program at the University of San Diego.

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

The main purpose of this project is to develop a school-level Early Warning System (EWS) that predicts which California public high schools are at risk of low graduation outcomes using only publicly available, non-PII education datasets. Unlike traditionaly EWS system that include sensitive student-level identifiers which are protected under FERPA, this project shows that meaninful early-warning signals can be derived entirely from open data aligned to the ABC framework: Attendance (A), Behavior (B), and Course performance (C).   

This work aims to give California educators, policy makers, and district leaders a scalable way to monitor emerging risk, identify structure inequities, and support strategic resource allocation. The project also contributes to the research gap on school-level predictors of graduation outcomes and evaluates whether open data can approximate the predictive capability of student-level systems.

# Partner(s)/Contributor(s)

- [Amayrani Balbuena](https://github.com/amayranib)
- [Jun Clemente](https://github.com/junclemente)
- [Tanya Ortega](https://github.com/tanyaort)

# Methods Used

A few examples are:
• Inferential Statistics
• Data Mining
• Predictive Modeling
• Machine Learning
• Data Visualization
• Data Engineering
• Text Mining
• Programming
• Data Manipulation
• Case Studies
• etc.

# Technologies

A few examples are:
• Python
• R
• SQL
• PostGres, MySql
• HTML
• JavaScript
• etc.

# Project Description

Discuss the details of project overview. Description your selected dataset, such as data source,
number of variables, size of dataset, etc. Include data dictionary if, available. Provide questions
and hypothesis that you are exploring. What specific data analysis, visualization, and modeling
work are you using to solve the problem? What roadblocks and challenges are you facing? etc.

# License

You can add under what license your project is. As a good practice, add LICENSE file in your
project folder as well.

# Acknowledgments

You can mention and thank those who technically helped you during the project.
