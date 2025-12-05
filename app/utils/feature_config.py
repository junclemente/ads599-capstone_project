"""
Shared configuration for ABC(S) feature groups and slider settings.
Used in both the ABCS page and the Feature Importance page.
"""

def get_slider_step(feature):
    default = slider_settings[feature]["default"]
    return 0.01 if isinstance(default, float) else 1


# --- ABCS Feature Groups ----------------------------------------------------

attendance_features = [
    "still_enrolled_rate",
    "chronicabsenteeismrate",
    "unexcused_absences_percent",
    "grade_retention_ratio",
]

behavior_features = [
    "stu_psv_ratio",      # pupil-services (counselors, support staff)
    "stu_adm_ratio",      # admin ratio (leadership/behavior systems)
]

course_features = [
    "met_uccsu_grad_reqs_rate",
    "pct_senior_cohort",
    "cohortstudents",
]

support_features = [
    "pct_experienced",
    "stu_tch_ratio",
    "percent__eligible_free_k12",
    "frpm_count_k12",
    "pct_bachelors_plus",
    "pct_bachelors",
]

# Combined list (optional helper)
all_features = (
    attendance_features
    + behavior_features
    + course_features
    + support_features
)

# --- Slider Settings --------------------------------------------------------


slider_settings = {
    "still_enrolled_rate": {
        "min": 0.0, "max": 20.0, "default": 5.0,
        "label": "Still Enrolled Rate (%)",
        "description": "Percent of the original graduation cohort still enrolled after 4 years without graduating.",
    },
    "chronicabsenteeismrate": {
        "min": 0.0, "max": 90.0, "default": 15.0,
        "label": "Chronic Absenteeism (%)",
        "description": "Percent of students missing 10% or more of instructional days.",
    },
    "unexcused_absences_percent": {
        "min": 0.0, "max": 100.0, "default": 25.0,
        "label": "Unexcused Absences (%)",
        "description": "Percent of all absences that are unexcused.",
    },
    "grade_retention_ratio": {
        "min": 0.0, "max": 3.0, "default": 1.0,
        "label": "Grade Retention Ratio",
        "description": "Ratio of students retained (repeating a grade) relative to the cohort size.",
    },

    "stu_psv_ratio": {
        "min": 0.0, "max": 4000.0, "default": 300.0,
        "label": "Students per Support Staff",
        "description": "Number of students per pupil-services staff (counselors, psychologists, social workers).",
    },
    "stu_adm_ratio": {
        "min": 0.0, "max": 2500.0, "default": 400.0,
        "label": "Students per Admin",
        "description": "Number of students per administrator (principal, APs, etc.).",
    },

    "met_uccsu_grad_reqs_rate": {
        "min": 0.0, "max": 100.0, "default": 60.0,
        "label": "Met UC/CSU Requirements (%)",
        "description": "Percent of graduates meeting A–G UC/CSU entrance requirements.",
    },
    "pct_senior_cohort": {
        "min": 0.0, "max": 1.0, "default": 0.50,
        "label": "Pct Seniors (0–1)",
        "description": "Share of all enrolled high school students who are 12th graders.",
    },
    "cohortstudents": {
        "min": 0, "max": 1200, "default": 400,
        "label": "Cohort Size",
        "description": "Number of students in the 4-year graduation cohort.",
    },

    "pct_experienced": {
        "min": 0.0, "max": 1.0, "default": 0.85,
        "label": "Pct Experienced Teachers (0–1)",
        "description": "Proportion of teachers classified as experienced by CDE.",
    },
    "stu_tch_ratio": {
        "min": 3.0, "max": 40.0, "default": 22.0,
        "label": "Student–Teacher Ratio",
        "description": "Average number of students per full-time equivalent teacher.",
    },
    "percent__eligible_free_k12": {
        "min": 0.0, "max": 1.0, "default": 0.50,
        "label": "FRPM Eligible (0–1)",
        "description": "Proportion of K–12 students eligible for free or reduced-price meals.",
    },
    "frpm_count_k12": {
        "min": 0, "max": 4000, "default": 800,
        "label": "FRPM Count",
        "description": "Number of K–12 students eligible for free or reduced-price meals.",
    },
    "pct_bachelors_plus": {
        "min": 0.0, "max": 1.0, "default": 0.25,
        "label": "Pct Bachelor’s+ (0–1)",
        "description": "Share of teachers with education beyond a bachelor’s degree (e.g., MA or post-BA credential).",
    },
    "pct_bachelors": {
        "min": 0.0, "max": 1.0, "default": 0.25,
        "label": "Pct Bachelor’s (0–1)",
        "description": "Share of teachers whose highest degree is a bachelor’s.",
    },
}
