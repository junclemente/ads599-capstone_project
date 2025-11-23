#import libraries 
import streamlit as st
import joblib 
import pandas as pd 

from pathlib import Path 
from utils.paths import get_paths

paths = get_paths()
MODELS_DIR = paths["MODELS_DIR"]


st.set_page_config(page_title="ABCS Predictors", layout="wide")
st.title("ABCS Predictor Inputs")



# # set paths - notebooks AND .py scripts
# if "__file__" in globals():
#     BASE_DIR = Path(__file__).resolve().parent
# else:
#     BASE_DIR = Path.cwd()


# print(BASE_DIR)
MODEL_PATH = MODELS_DIR / "random_forest_ews.pkl"
FEATURE_PATH = MODELS_DIR / "top_features.pkl"

# load models/features
top_features = joblib.load(FEATURE_PATH)
model = joblib.load(MODEL_PATH)

st.header("Feature Inputs by ABCS Categories")



attendance_features = [
    "still_enrolled_rate",
    "chronicabsenteeismrate",
    "unexcused_absences_percent",
    "grade_retention_ratio"
]

behavior_features = [
    "stu_psv_ratio",  # pupil-services (counselor/support)
    "stu_adm_ratio"   # admin ratio (leadership/behavior systems)
]

course_features = [
    "met_uccsu_grad_reqs_rate",
    "pct_senior_cohort",
    "cohortstudents"
]

support_features = [
    "pct_experienced",
    "stu_tch_ratio",
    "percent__eligible_free_k12",
    "frpm_count_k12",
    "pct_bachelors_plus",
    "pct_bachelors"
]

# slider settings 

slider_settings = {
    "still_enrolled_rate":        {"min": 0.0, "max": 20.0, "default": 5.0, "label": "Still Enrolled Rate (%)"},
    "chronicabsenteeismrate":     {"min": 0.0, "max": 90.0, "default": 15.0, "label": "Chronic Absenteeism (%)"},
    "unexcused_absences_percent": {"min": 0.0, "max": 100.0, "default": 25.0, "label": "Unexcused Absences (%)"},
    "grade_retention_ratio":      {"min": 0.0, "max": 3.0, "default": 1.0,  "label": "Grade Retention Ratio"},

    "stu_psv_ratio":              {"min": 0.0, "max": 4000.0, "default": 300.0, "label": "Students per Support Staff"},
    "stu_adm_ratio":              {"min": 0.0, "max": 2500.0, "default": 400.0, "label": "Students per Admin"},

    "met_uccsu_grad_reqs_rate":   {"min": 0.0, "max": 100.0, "default": 60.0, "label": "Met UC/CSU Requirements (%)"},
    "pct_senior_cohort":          {"min": 0.0, "max": 1.0,   "default": 0.50, "label": "Pct Seniors (0–1)"},
    "cohortstudents":             {"min": 0,   "max": 1200,  "default": 400,  "label": "Cohort Size"},

    "pct_experienced":            {"min": 0.0, "max": 1.0,   "default": 0.85, "label": "Pct Experienced Teachers (0–1)"},
    "stu_tch_ratio":              {"min": 3.0, "max": 40.0,  "default": 22.0, "label": "Student–Teacher Ratio"},
    "percent__eligible_free_k12": {"min": 0.0, "max": 1.0,   "default": 0.50, "label": "FRPM Eligible (0–1)"},
    "frpm_count_k12":             {"min": 0,   "max": 4000,  "default": 800,  "label": "FRPM Count"},
    "pct_bachelors_plus":         {"min": 0.0, "max": 1.0,   "default": 0.25, "label": "Pct Bachelor’s+ (0–1)"},
    "pct_bachelors":              {"min": 0.0, "max": 1.0,   "default": 0.25, "label": "Pct Bachelor’s (0–1)"},
}



# create 4 columns
col_A, col_B, col_C, col_S = st.columns(4)

# dictionary to hold slider values 
feature_inputs = {}

# A - Attendance
with col_A:
    st.subheader("A: Attendance")
    for feature in attendance_features:
        s = slider_settings[feature]
        st.session_state[feature] = st.slider(
            s["label"], s["min"], s["max"], s["default"]
        )

# B - Behavior / Climate Support 
with col_B:
    st.subheader("B: Behavior")
    for feature in behavior_features:
        s = slider_settings[feature]
        st.session_state[feature] = st.slider(
            s["label"], s["min"], s["max"], s["default"]
        )

# C — COURSE PERFORMANCE
with col_C:
    st.subheader("C: Course")
    for feature in course_features:
        s = slider_settings[feature]
        st.session_state[feature] = st.slider(
            s["label"], s["min"], s["max"], s["default"]
        )


# S — SCHOOL / CONTEXT SUPPORTS
with col_S:
    st.subheader("S: Supports")
    for feature in support_features:
        s = slider_settings[feature]
        st.session_state[feature] = st.slider(
            s["label"], s["min"], s["max"], s["default"]
        )


# Model prediction 

# create dataframe of values
input_df = pd.DataFrame({
    feature: [st.session_state[feature]]
    for feature in (
        attendance_features +
        behavior_features + 
        course_features + 
        support_features
    )
})

# reorder feature values to match top_features and as expected by model
input_df = input_df.reindex(columns=top_features)

# debug check if df features matches model
# st.write("Order matches:", list(input_df.columns) == top_features)

st.divider()

prediction = model.predict(input_df)[0]
risk_label = "At Risk" if prediction == 1 else "On Track"
st.subheader(f"Model Prediction: {risk_label}")

probability = model.predict_proba(input_df)[0][1]
st.write(f"Risk Probability: {round(probability * 100,1)}%")
# st.progress(probability)

st.divider() 

st.markdown("### Understanding the ABCS Categories")

colA, colB, colC, colS = st.columns(4)

with colA:
    st.subheader("A: Attendance")
    st.markdown(
        """
        Attendance indicators capture how consistently students are present in school. 
        Chronic absenteeism and unexcused absences are among the strongest predictors of dropout risk.
        """
    )

with colB:
    st.subheader("B: Behavior")
    st.markdown(
        """
        Behavior reflects school climate and student engagement. 
        Supports such as counselor availability and administrative leadership shape behavior, belonging, and safety.
        """
    )

with colC:
    st.subheader("C: Course")
    st.markdown(
        """
        Course performance measures student progress toward graduation expectations — including UC/CSU requirements, senior cohort progression, and credit completion.
        """
    )

with colS:
    st.subheader("S: Supports")
    st.markdown(
        """
        School supports represent the resources available to students: experienced teachers, reasonable class sizes, and the socioeconomic context of the school community.
        """
    )
