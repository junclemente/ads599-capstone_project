# 📘 Data Dictionary - Final Top 15 Features 

This section documents the final **Top 15 features** selected for the Early Warning System (EWS) predictive modeling. These variables represent the strongest predictors of high school graduation outcomes based on feature importance analyses conducted during model development (Random Forest, Gradient Boosting, and correlation-based selection). Each feature listed below includes its unit type, source, construct, and its role within the ABC Early Warning framework or structural school capacity domain. This refined feature set serves as the input to the final classification models and reflects the variables most strongly associated with graduation risk across California public high schools.

| Feature                      | Unit Type              | What it Measures                                            | Source / Construct      | Why it Matters (EWS/Grad Risk)                                          |
| ---------------------------- | ---------------------- | ----------------------------------------------------------- | ----------------------- | ----------------------------------------------------------------------- |
| `still_enrolled_rate`        | **Percent (0–100)**    | % of cohort still enrolled after 4 years without graduating | CDE ACGR                | High values indicate delayed completion / dropout risk.                 |
| `chronicabsenteeismrate`     | **Percent (0–100)**    | % of students chronically absent (miss ≥10% days)           | CDE Chronic Absenteeism | Classic Attendance EWS indicator; linked to non-grad risk.              |
| `unexcused_absences_percent` | **Percent (0–100)**    | % of absences that are unexcused                            | CalSCHLS / attendance   | Behavior/engagement risk signal.                                        |
| `met_uccsu_grad_reqs_rate`   | **Percent (0–100)**    | % of grads meeting UC/CSU A–G requirements                  | CDE ACGR                | Academic rigor / college readiness proxy.                               |
| `percent__eligible_free_k12` | **Proportion (0–1)**   | Share of students eligible for FRPM                         | CDE FRPM                | Socioeconomic disadvantage predictor.                                   |
| `frpm_count_k12`             | **Count**              | Number of FRPM-eligible students                            | CDE FRPM                | Context for school poverty scale; also correlates with enrollment size. |
| `stu_tch_ratio`              | **Ratio (continuous)** | Students per teacher                                        | CDE Staff Assignment    | Classroom load / instructional capacity proxy.                          |
| `pct_experienced`            | **Proportion (0–1)**   | Share of teachers with ≥3 years experience                  | CDE Staff Assignment    | Teacher stability/quality indicator.                                    |
| `cohortstudents`             | **Count**              | Size of adjusted 9th-grade cohort tracked for ACGR          | CDE ACGR                | School size context; affects resource strain and rate stability.        |
| `pct_senior_cohort`          | **Proportion (0–1)**   | Share of enrollment that is grade-12 students               | CDE Enrollment          | Retention/composition indicator; low senior share can signal attrition. |
| `stu_adm_ratio`              | **Ratio (continuous)** | Students per administrator                                  | CDE Staff Assignment    | Leadership load / admin capacity proxy.                                 |
| `grade_retention_ratio`      | **Ratio (continuous)** | Rate/ratio of students repeating a grade                    | CDE Student Performance | Academic struggle early warning signal.                                 |
| `pct_bachelors_plus`         | **Proportion (0–1)**   | Share of teachers with post-BA coursework                   | CDE Staff Experience    | Professional development / qualification depth.                         |
| `stu_psv_ratio`              | **Ratio (continuous)** | Students per pupil-services staff (counselors etc.)         | CDE Staff Assignment    | Access to support services; lower support → higher risk.                |
| `pct_bachelors`              | **Proportion (0–1)**   | Share of teachers with a bachelor’s degree                  | CDE Staff Experience    | Baseline staff qualification indicator.                                 |

---

# Attendance Indicators (A) - Student Presence & Engagement

These features capture whether studens are actually present and engaged in school.

| Feature                      | Why It Matters                                                                                                                          |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `chronicabsenteeismrate`     | Chronic absenteeism is one of the strongest predictors of dropout; missing 10%+ of days disrupts academic momentum (AIR, EWS research). |
| `unexcused_absences_percent` | High unexcused absence rates indicate disengagement and weak school-family connections.                                                 |
| `still_enrolled_rate`        | High % still enrolled after 4 years suggests delayed pathways or risk of non-completion.                                                |

# Behavior and Engagement Indicators (B) - Discipline, Support, and Student Stability

| Feature                 | Why It Matters                                                                                                       |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `stu_psv_ratio`         | Students per counselor/psychologist; limited support staff increases unresolved behavioral and mental health issues. |
| `grade_retention_ratio` | Grade retention is a documented early warning flag; retained students are significantly more likely to not graduate. |
| `pct_experienced`       | Experienced teachers manage classrooms more effectively and foster engagement.                                       |

# Course-Performance / Academic Indicators (C) - Coursework, Rigor, and Achievement

| Feature                    | Why It Matters                                                                                   |
| -------------------------- | ------------------------------------------------------------------------------------------------ |
| `met_uccsu_grad_reqs_rate` | Completing UC/CSU A–G requirements reflects academic rigor and predicts postsecondary readiness. |
| `pct_bachelors_plus`       | Higher teacher qualification levels correlate with stronger instructional quality.               |
| `pct_bachelors`            | Indicates baseline teacher preparation; impacts course delivery quality.                         |
| `pct_senior_cohort`        | Low senior proportion can indicate earlier grade attrition.                                      |

# Structural & Contextual School Factors (S) - Capacity, Resources, and Socioeconomic Risk

Although these variables are not formally categorized within the ABC early warning framework, they strongly influence a school's overall ability to support at-risk students through identification and intervention.

| Feature                      | Why It Matters                                                                                       |
| ---------------------------- | ---------------------------------------------------------------------------------------------------- |
| `frpm_count_k12`             | High counts reflect concentrated poverty; poverty strongly correlates with graduation challenges.    |
| `percent__eligible_free_k12` | Proportion of economically disadvantaged students; systemic risk indicator.                          |
| `stu_tch_ratio`              | Larger class sizes reduce individual support and impede learning recovery.                           |
| `stu_adm_ratio`              | High student–administrator ratios strain leadership capacity and monitoring systems.                 |
| `cohortstudents`             | Cohort size impacts resource allocation, intervention load, and stability of graduation percentages. |

---
