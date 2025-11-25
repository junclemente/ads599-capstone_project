# 📘 Data Dictionary - Combined EDA Dataset

**Initial EWS Dataset (Combined, Pre-Modeling Version)**
This data dictionary provides definitions for all variables included in the combined Early Warning System (EWS) dataset used during the Exploratory Data Analysis (EDA) phase. The dataset integrates multiple publicly available sources from the California Department of Education (CDE)—including graduation outcomes, absenteeism, staffing, socioeconomic indicators, and school climate data—into a unified analytic file. Each variable listed is accompanied by its source system, data type, description, and analytic relevance. This reference supports transparency, ensures reproducibility, and documents how each feature contributes to understanding early-risk signals for high school graduation outcomes.

---

## 🧭 Variable Reference

| **Feature**                               | **Source**                 | **Type**            | **Description**                                                     | **Analytical Purpose**                              |
| ----------------------------------------- | -------------------------- | ------------------- | ------------------------------------------------------------------- | --------------------------------------------------- |
| `cdscode`                                 | Public Schools & Districts | String              | 14-digit unique identifier for each school (County–District–School) | Primary key for merging all datasets                |
| `county`                                  | Public Schools & Districts | String              | County name where the school is located                             | Used to join county-level climate data              |
| `charter`                                 | Public Schools & Districts | Categorical (Y/N)   | Indicates whether the school is a charter                           | Filtered to include only traditional public schools |
| `eilcode`                                 | Public Schools & Districts | String              | Educational Instruction Level (e.g., HS)                            | Identifies high schools for inclusion               |
| `virtual`                                 | Public Schools & Districts | Categorical (Y/N/V) | Indicates level of virtual instruction                              | Contextual feature on school modality               |
| `magnet`                                  | Public Schools & Districts | Categorical (Y/N)   | Indicates whether a school offers a magnet program                  | Structural feature; possible equity proxy           |
| `yearroundyn`                             | Public Schools & Districts | Categorical (Y/N)   | Indicates whether the school uses a year-round calendar             | Operational characteristic                          |
| `latitude`                                | Public Schools & Districts | Float               | School’s latitude coordinate                                        | Used for mapping and regional analysis              |
| `longitude`                               | Public Schools & Districts | Float               | School’s longitude coordinate                                       | Used for mapping and regional analysis              |
| `multilingual`                            | Public Schools & Districts | Categorical (Y/N)   | Indicates if the school offers multilingual programs                | Cultural/linguistic inclusivity indicator           |
| `cohortstudents`                          | ACGR                       | Float               | Number of students in the four-year graduation cohort               | Used for weighting and validation                   |
| `regular_hs_diploma_graduates_rate`       | ACGR                       | Float               | Percent of students earning a regular high school diploma           | **Primary target variable**                         |
| `met_uccsu_grad_reqs_rate`                | ACGR                       | Float               | Percent meeting UC/CSU A–G requirements                             | College readiness indicator                         |
| `seal_of_biliteracy_rate`                 | ACGR                       | Float               | Percent earning the Seal of Biliteracy                              | Academic achievement proxy                          |
| `dropout_rate`                            | ACGR                       | Float               | Percent of students who dropped out                                 | Negative outcome indicator                          |
| `still_enrolled_rate`                     | ACGR                       | Float               | Percent still enrolled after four years                             | Persistence indicator                               |
| `chronicabsenteeismrate`                  | Chronic Absenteeism        | Float               | Percent of students chronically absent                              | Attendance component (EWS “A”)                      |
| `eligible_cumulative_enrollment`          | Absence by Reason          | Integer             | Count of eligible students for absence calculations                 | Denominator for absence-based metrics               |
| `unexcused_absences_percent`              | Absence by Reason          | Float               | Percent of absences that were unexcused                             | Behavior/engagement proxy (EWS “B”)                 |
| `outofschool_suspension_absences_percent` | Absence by Reason          | Float               | Percent of absences due to out-of-school suspension                 | Behavior indicator (EWS “B”)                        |
| `percent__eligible_free_k12`              | FRPM                       | Float               | Percent of K–12 students eligible for free meals                    | Socioeconomic disadvantage proxy                    |
| `frpm_count_k12`                          | FRPM                       | Integer             | Count of FRPM-eligible students                                     | Enrollment scale/context                            |
| `calpads_fall_1_certification_status`     | FRPM                       | Categorical (Y/N)   | Indicates CALPADS certification status                              | Data quality flag                                   |
| `school_grade_span`                       | Student–Staff Ratio        | String              | Grade span served (e.g., GS_K12)                                    | Used to subset and interpret ratios                 |
| `stu_tch_ratio`                           | Student–Staff Ratio        | Float               | Student-to-teacher ratio                                            | Instructional capacity indicator                    |
| `stu_adm_ratio`                           | Student–Staff Ratio        | Float               | Student-to-administrator ratio                                      | Administrative load indicator                       |
| `stu_psv_ratio`                           | Student–Staff Ratio        | Float               | Student-to-pupil services ratio                                     | Support services capacity                           |
| `pct_associate`                           | Staff Education            | Float               | Percent of staff with associate degrees                             | Faculty qualification mix                           |
| `pct_bachelors`                           | Staff Education            | Float               | Percent of staff with bachelor’s degrees                            | Faculty qualification mix                           |
| `pct_bachelors_plus`                      | Staff Education            | Float               | Percent of staff with bachelor’s + credential                       | Teacher certification measure                       |
| `pct_master`                              | Staff Education            | Float               | Percent of staff with master’s degrees                              | Professional attainment indicator                   |
| `pct_master_plus`                         | Staff Education            | Float               | Percent of staff with master’s + credential                         | Advanced credentialing indicator                    |
| `pct_doctorate`                           | Staff Education            | Float               | Percent of staff with doctoral degrees                              | High academic qualification indicator               |
| `pct_juris_doctor`                        | Staff Education            | Float               | Percent of staff with juris doctor degrees                          | Specialized degree indicator                        |
| `pct_no_degree`                           | Staff Education            | Float               | Percent of staff with no degree                                     | Low qualification indicator                         |
| `pct_experienced`                         | Staff Experience           | Float               | Percent of staff with ≥3 years of experience                        | Staff stability indicator                           |
| `pct_inexperienced`                       | Staff Experience           | Float               | Percent of staff with <3 years of experience                        | Novice staff indicator                              |
| `pct_first_year`                          | Staff Experience           | Float               | Percent of staff in their first year                                | Staff turnover/instability proxy                    |
| `pct_second_year`                         | Staff Experience           | Float               | Percent of staff in their second year                               | Early-career staff indicator                        |
| `grade_retention_ratio`                   | Enrollment by Grade        | Float               | Ratio of 12th- to 9th-grade enrollment                              | Cohort progression indicator                        |
| `pct_hs_enrollment`                       | Enrollment by Grade        | Float               | Percent of total enrollment in grades 9–12                          | High school representation                          |
| `pct_senior_cohort`                       | Enrollment by Grade        | Float               | Percent of total enrollment in grades 11–12                         | Cohort proximity to graduation                      |
| `pct_unsafe_gr11`                         | CalSCHLS (Safety)          | Float               | Percent of 11th graders reporting unsafe or very unsafe             | Perceived safety risk indicator                     |
| `pct_safe_gr11`                           | CalSCHLS (Safety)          | Float               | Percent of 11th graders reporting safe or very safe                 | Positive safety perception                          |
| `pct_neutral_gr11`                        | CalSCHLS (Safety)          | Float               | Percent reporting neither safe nor unsafe                           | Neutral climate perception                          |
| `avg_safety_score`                        | CalSCHLS (Connectedness)   | Float               | Weighted average of safety indicators                               | Aggregated safety measure                           |
| `high_conn`                               | CalSCHLS (Connectedness)   | Float               | Share of students reporting high connectedness                      | Engagement indicator                                |
| `low_conn`                                | CalSCHLS (Connectedness)   | Float               | Share of students reporting low connectedness                       | Disengagement risk indicator                        |
| `conn_ratio`                              | CalSCHLS (Connectedness)   | Float               | Ratio of high to low connectedness                                  | Climate balance index                               |
| `school_climate_index`                    | CalSCHLS (Connectedness)   | Float               | Composite index combining safety and connectedness                  | Overall school climate score                        |

---

## 🗂️ Notes

- All datasets were merged at the school level using `cdscode` as the unique identifier.
- County-level safety and connectedness features were merged using standardized county names.
- Percentage-based fields were cleaned and standardized across sources.
- Suppressed or missing values reflect CDE privacy rules or unavailable county climate data.

---
