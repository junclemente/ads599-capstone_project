# Abstract

California’s overall graduation rate hides important gaps for English learners, students with disabilities, and foster youth. This project develops a school-level Early Warning System (EWS) that identifies high schools at risk of low graduation rates using only publicly available data compliant with the Family Education Rights and Privacy Act (FERPA). Multiple statewide datasets, including ACGR, chronic absenteeism, FRPM eligibility, and staffing, were combined and aligned with the ABC framework. A Random Forest model achieved strong performance (PR-AUC = 0.78) and identified attendance, socioeconomic indicators, and still-enrolled rates as the strongest predictors. The results show that publicly available data can approximate traditional EWS insights and support scalable, privacy-preserving approaches to identifying emerging graduation-risk patterns.

<br>

# Table of Contents

1. [Abstract](#abstract)
2. [Business Background](#business-background)
3. [Problem Statement](#problem-statement)
4. [Summary of Findings](#summary-of-findings)
5. [Business Questions](#business-questions)
6. [Scope of Analysis](#scope-of-analysis)
7. [Approach](#approach)
8. [Limitations](#limitations)
9. [Solution Details](#solution-details)
10. [Concluding Summary](#concluding-summary)
11. [Call to Action](#call-to-action)
12. [References](#references)

<br>

## Business Background

Attaining a high school diploma significantly improves students’ long-term employment and economic opportunities, while students who do not graduate face greater barriers, such as limited job prospects and lower lifetime earnings (Krueger et al., 2015). Even though these impacts are well-documented, thousands of California students still drop out each year.

In 2021–2022, California’s overall graduation rate was 87%, measured using the four-year Adjusted Cohort Graduation Rate (ACGR). However, statewide averages hide important differences: groups such as English learners, students with disabilities, and foster youth continue to graduate at rates below 80%, a trend that has remained consistent over time (California Department of Education, 2023).

To help identify emerging dropout risks, a lot of districts use Early Warning Systems (EWS) that track the “ABC” indicators: attendance, behavior, and course performance. Research shows that these models can effectively predict dropout risk (O’Cummings & Therriault, 2015; Rumberger et al., 2017). However, traditional EWS rely on student-level data that is protected under FERPA, making statewide scaling difficult.

These gaps highlight the need for tools that can scale, protect student privacy, and still provide a way to identify schools where graduation rates may be starting to decline.

<br>

## Problem Statement

California continues to see large graps in graduation rates, especially for English learners, foster youth, and students with disabilities. While statewide accountability tools such as the California School Dashboard report historical outcomes, they do not identify emerging risk factors or predict which schools may experience declining graduation rates.

District-level Early Warning Systems exist, but they rely on restricted student-level data protected under FERPA, which limits access for researchers, policymakers, and education stakeholders. As a result, California does not have a scalable, publicly accessible method for assessing school-level graduation risk.

This project addresses this gap by developing a predictive model using only publicly available school-level datasets from the California Department of Education. By aligning open data with the ABC early-warning framework, the model aims to identify high schools at risk of graduating fewer than 90% of their students while maintaining full compliance with data privacy requirements.

<br>

## Summary of Findings

- **Random Forest** achieved the strongest performance (PR-AUC = 0.78), with Logistic Regression and Naive Bayes close behind.
- The most influential predictors aligned with the ABC framework:
  - **Attendance:** chronic absenteeism, unexcused absences
  - **Behavior/Course performance:** still-enrolled rate, A–G completion
  - **Socioeconomic factors:** FRPM eligibility
  - **Support indicators:** teacher experience and staffing patterns
- Climate variables (CalSCHLS) did not meaningfully contribute to prediction and were excluded due to missingness.
- A 90% graduation-rate threshold produced a manageable class distribution and allowed consistent risk identification without resampling.
- Results confirm that public, non-PII school-level data can approximate the predictive insights of student-level Early Warning Systems.

<br>

## Business Questions

This project is guided by the following core questions:

1. **Signal & prediction**

   - To what extent can publicly available, school-level data from the California Department of Education (CDE) be used to predict whether a high school is at risk of graduating fewer than 90% of its students?

2. **Key drivers**

   - Which school-level indicators, especially those aligned with the Attendance, Behavior, and Course performance (ABC) framework, are most strongly associated with low graduation outcomes?

3. **Equity & disproportionality**

   - How do attendance, socioeconomic, and staffing patterns relate to graduation disparities for schools serving higher proportions of historically underserved students?

4. **Model performance & reliability**

   - Among commonly used classification algorithms, which models provide the most reliable performance on imbalanced graduation outcomes when trained solely on open, school-level data?

5. **Practical deployment**

   - Can the final model be deployed as an accessible, interactive tool (e.g., via a Streamlit application) that allows education leaders to explore predicted graduation risk and understand the factors driving those predictions?

6. **Scalability & replication**
   - Does this approach provide a scalable, privacy-preserving template that could be adapted to additional years or other states using similar publicly reported education data?

<br>

## Scope of Analysis

This analysis focuses on developing a school-level Early Warning System (EWS) for predicting low graduation outcomes using only publicly available California Department of Education (CDE) datasets. The scope includes both the elements incorporated into the study and those intentionally excluded to ensure data quality, methodological consistency, and compliance with FERPA.

### Included in Scope

- **School-level data only:**  
  All predictors were drawn from publicly accessible CDE reporting systems for the 2021–22 academic year.
- **Multiple statewide datasets combined:**
  Graduation outcomes (ACGR), absenteeism, student poverty (FRPM), staffing and teacher experience, enrollment, and school directory files were merged to create a unified school-level dataset. County-level school climate indicators (CalSCHLS 2017–19) were reviewed, though ultimately excluded from the final model.
- **ABC Framework alignment:**  
  Attendance, Behavior, and Course performance indicators were prioritized for modeling.
- **High school population:**  
  The analysis includes California public high schools with valid cohort sizes and complete graduation outcomes.
- **Binary risk classification:**  
  Schools were labeled “At Risk” if their graduation rate was below 90%, providing an early-warning threshold rather than a failing benchmark.
- **Multiple machine learning models:**  
  Seven supervised classification algorithms were tested and compared using imbalance-appropriate metrics (precision, recall, F1, PR-AUC).

### Excluded from Scope

- **Student-level data:**  
  FERPA-protected records and individual student indicators were excluded entirely.
- **Schools without valid ACGR data:**  
  Schools missing graduation rates or reporting fewer than 90% of expected cohort enrollment were removed for data quality.
- **Limited climate data availability:**  
  The most recent CalSCHLS climiate indicators (2017-2019) were explored during EDA, but excluded from the final model because seven counties did not have any data and the variables did not improve predictive performance.
- **Non-high school institutions:**  
  Middle schools, continuation schools, juvenile court schools, and alternative education programs were excluded.
- **Model optimization:**  
  Hyperparameter tuning was not performed; models were compared using baseline settings to evaluate feasibility rather than maximize performance.

### Scope Rationale

Limiting the analysis to publicly available school-level data ensures full compliance with state and federal privacy regulations while supporting scalability, transparency, and reproducibility. Excluding datasets with significant missingness or limited predictive value helps maintain the reliability of the final model. Overall, the scope is designed to answer the core question of whether open, non-sensitive data can provide early-warning insights traditionally derived from student-level systems.

<br>

## Approach

The development of a school-level Early Warning System (EWS) followed a structured, multi-stage process aligned with best practices in data preparation, exploratory analysis, and supervised machine learning. The goal was to determine whether publicly available CDE datasets could reliably predict graduation risk while remaining fully compliant with FERPA.

### 1. Data Acquisition and Integration

Multiple publicly accessible CDE reporting systems were used to build the unified school-level dataset, including graduation outcomes (ACGR), chronic absenteeism, FRPM eligibility, staffing and teacher experience, enrollment, and school directory files. Each dataset was cleaned, standardized, and merged using the 14-digit CDS code as the unique school identifier. Records were filtered to retain only California public high schools with valid cohort data and active reporting status.

### 2. Exploratory Data Analysis (EDA)

EDA was performed to assess distributions, detect anomalies, and evaluate missingness. Patterns were reviewed across attendance, coursework, staffing, and socioeconomic indicators. We examined skewness, outliers, and correlations to understand the relationships between predictors and graduation outcomes. Class imbalance was confirmed, with most schools reporting high graduation rates.

### 3. Data Quality Assessment

Variables with inconsistent reporting, low variance, or structural missingness were flagged for removal. CalSCHLS climate indicators were explored but excluded because data were missing for seven counties and the variables did not improve model performance. Remaining missing values in staffing and enrollment fields were imputed using median values.

### 4. Feature Engineering

Feature selection and engineering focused on strengthening alignment with the ABC framework. Non-informative and redundant variables (e.g., climate-connectedness indicators, geographic identifiers, low-variance categories) were removed. A binary target variable was constructed using a 90% graduation-rate threshold to support early-warning risk classification. The final modeling dataset included the 15 strongest predictors identified through Random Forest importance rankings.

### 5. Model Development and Evaluation

Seven supervised learning algorithms were trained for comparison: Logistic Regression, Naive Bayes, Random Forest, Support Vector Machine (SVM), K Nearest Neighbors (KNN), Decision Tree, and XGBoost. An 80/20 stratified split was used to address class imbalance. Model performance was evaluated using precision, recall, F1 score, and PR-AUC, since accuracy is not meaningful for imbalanced outcomes. No synthetic resampling methods were applied; instead, stratification and class weighting were used to ensure fair evaluation. The Random Forest model achieved the highest PR-AUC (0.78) and demonstrated the most consistent performance across thresholds.

### 6. Deployment and Visualization

To support practical adoption, the final model was integrated into an interactive Streamlit application that allows users to adjust key indicators and view real-time predictions. The app also summarizes predictor importance, enabling education leaders to interpret contributing factors and explore risk scenarios for California high schools.

<br>

## Limitations

While this study demonstrates that school-level, publicly available data can be used to predict low graduation outcomes, several limitations should be considered when interpreting results and applying the model.

### 1. Limited Availability of School-Climate Data

School climate and safety indicators from CalSCHLS were only available at the county level for 2017–2019, and data were missing for seven counties. Since these indicators did not improve model performance, they were excluded. Consequently, the model does not fully incorporate behavioral or engagement-related climate factors that influence graduation outcomes.

### 2. Constraints of School-Level Aggregation

The analysis uses aggregated, school-level indicators rather than student-level data. While appropriate for privacy and scalability, school-level variables cannot capture individual patterns of disengagement, subgroup differences, or student-level pathways that may contribute to graduation disparities.

### 3. FERPA-Driven Data Suppression

Several CDE reporting systems suppress outcomes for small subgroups to protect student privacy. This results in structural missingness in certain fields—especially absenteeism subgroups and low-frequency indicators—which may limit model granularity.

### 4. Limited Generalizability Beyond California

The model is designed specifically for California’s reporting structure, data availability, and accountability framework. States with different data systems or different definitions of graduation metrics may require adjustments to replicate this approach.

### 5. Class Imbalance and Model Baseline Scope

Because most California high schools graduate more than 90% of students, the dataset is inherently imbalanced. Although PR-AUC and class weighting mitigate this, rare-at-risk schools may be harder to identify. Additionally, models were compared using baseline settings rather than full hyperparameter optimization, as the goal was feasibility rather than maximum performance.

Despite these limitations, the findings provide evidence that open, school-level data can serve as a practical foundation for scalable, privacy-preserving early warning analytics across California high schools.

<br>

## Solution Details

The resulting Early Warning System (EWS) provides a scalable, privacy-preserving approach for identifying California public high schools at risk of low graduation outcomes. Built entirely from publicly available school-level data, the system offers a practical alternative to traditional student-level EWS models that are restricted under FERPA and difficult to implement consistently across districts.

### A Simplified, School-Level Predictive Model

The final solution is a supervised machine learning model trained on multiple publicly available CDE reporting systems aligned with the Attendance, Behavior, and Course performance (ABC) framework. A Random Forest classifier was selected as the primary model because it achieved the strongest performance on imbalanced outcomes (PR AUC = 0.78) and provided interpretable feature rankings.

The model uses 15 key predictors, including chronic absenteeism, unexcused absences, FRPM eligibility, still enrolled rates, A-G completion, student teacher ratios, and teacher experience. Together, these indicators offer a streamlined and effective approach to identifying schools that may be at risk of lower graduation outcomes.

### Actionable Insights Through Predictor Importance

Feature importance analysis highlights the main drivers of school level graduation outcomes and aligns closely with well established early warning research. Attendance and engagement indicators were the strongest predictors, followed by socioeconomic and course completion measures. A fourth category also emerged in our analysis: School Support, reflected in factors such as teacher experience and staffing related measures at the school level.

These insights give school and district leaders a clearer understanding of the conditions most associated with lower graduation outcomes and help guide where early and targeted interventions may be needed.

### Interactive Risk Exploration Tool

To support practical adoption, the solution includes a publicly accessible Streamlit web application that allows users to:

- adjust key school indicators using interactive sliders,
- view real-time risk predictions based on the final Random Forest model,
- examine the relative importance of predictors,
- explore results without any need for coding or specialized software.

This tool provides an intuitive, user-friendly interface that districts, county offices, and policymakers can use to understand potential risk patterns and test “what-if” scenarios.

### Scalable and Replicable Framework

Because the system relies only on school-level, non-PII data that is released annually by the CDE, it can be easily updated for future school years and adapted for additional states with similar public reporting structures. The workflow is fully documented and reproducible, ensuring transparency and enabling districts to validate and extend the model as needed.

Overall, the solution demonstrates that publicly available data can support reliable early-warning insights while maintaining privacy, equity, and accessibility—key priorities for California’s education system.

<br>

## Concluding Summary

This project demonstrates that a simplified, school-level Early Warning System (EWS) can reliably identify California public high schools at risk of low graduation outcomes using only publicly available, non-PII data. By integrating multiple statewide datasets aligned with the ABC framework and evaluating seven supervised learning algorithms, we showed that publicly reported school indicators can approximate the predictive insights typically achieved using restricted student-level systems. The final Random Forest model delivered strong performance on imbalanced outcomes (PR-AUC = 0.78) and identified key predictors consistent with established research, including chronic absenteeism, unexcused absences, FRPM eligibility, and course-completion measures.

Importantly, the project provides an equitable and scalable framework for early-warning analytics across California’s diverse school system. Because the model relies exclusively on open data, it can be updated annually, replicated across districts, and adapted for use in other states with similar reporting structures while remaining fully compliant with federal privacy regulations.

Combined with an interactive Streamlit application that allows users to explore risk scenarios and examine predictor importance, this solution offers a practical foundation for supporting early intervention, guiding resource allocation, and strengthening educational outcomes in California’s public high schools.

<br>

## Call to Action

Education leaders, district administrators, researchers, and policymakers are encouraged to use the resources developed in this project to support data-informed decision-making and strengthen graduation outcomes across California high schools.

To explore the model and its insights:

- **Use the interactive Early Warning System application** to adjust key school indicators and view real-time risk predictions:  
  https://ca-early-warning-system.streamlit.app/

- **Review the full workflow, modeling code, and documentation** in the project’s GitHub repository to understand how the model was built, evaluated, and deployed.

- **Leverage the identified predictors**, especially chronic absenteeism, unexcused absences, FRPM eligibility, and A–G completion, to guide targeted interventions, resource allocation, and equity-focused planning.

- **Adapt and extend the framework** for additional school years, district-level analyses, or for use in other states with similar publicly reported data.

By engaging with these tools and insights, stakeholders can take actionable steps toward earlier identification of emerging risks, more strategic support for high-need schools, and more equitable educational outcomes across California.

<br>

## References

Austin, G., Hanson, T., Bala, N., & Zheng, C. (2023). Student engagement and well-being in California, 2019-21: Results of the Eighteenth Biennial State California Healthy Kids Survey, Grades 7, 9, and 11. WestEd. https://data.calschls.org/resources/18th_Biennial_State_1921.pdf

California Department of Education. (n.d.). Retrieved October 26, 2025, from https://www.cde.ca.gov/

Chen, T., Wanberg, R. C., Gouioa, E. T., Brown, M. J. S., Chen, J. C.-Y., & Kurt Kraiger, J. J. (2019). Engaging parents Involvement in K – 12 Online Learning Settings: Are We Meeting the Needs of Underserved Students? Journal of E-Learning and Knowledge Society, Vol 15 No 2 (2019): Journal of eLearning and Knowledge Society. https://doi.org/10.20368/1971-8829/1563

Cobb, C. D. (2020). Geospatial Analysis: A New Window Into Educational Equity, Access, and Opportunity. Review of Research in Education, 44(1), 97–129. https://doi.org/10.3102/0091732X20907362

Rumberger, R., Addis, H., Allensworth, E., Balfanz, R., Bruch, J., Dillon, E., Duardo, D., Dynarski, M., Furgeson, J., Jayanthi, M., Newman-Gonchar, R., Place, K., & Tuttle, C. (2017). Preventing Dropout in Secondary Schools (No. NCEE 2017-4028). National Center for Education Evaluation and Regional Assistance (NCEE), Institute of Education Sciences, U.S. Department of Education. https://whatworks.ed.gov

Sava, S., Bunoiu, M., & Malita, L. (2017). Ways to Improve Students’ Decision for Academic Studies. Acta Didactica Napocensia, 10(4), 109–120. https://doi.org/10.24193/adn.10.4.11

Siegle, D., Gubbins, E. J., O’Rourke, P., Langley, S. D., Mun, R. U., Luria, S. R., Little, C. A., McCoach, D. B., Knupp, T., Callahan, C. M., & Plucker, J. A. (2016). Barriers to Underserved Students’ Participation in Gifted Programs and Possible Solutions. Journal for the Education of the Gifted, 39(2), 103–131. https://doi.org/10.1177/0162353216640930

The California School Climate, Health, and Learning Survey (CalSCHLS) System—Home. (n.d.). Retrieved October 26, 2025, from https://calschls.org/
