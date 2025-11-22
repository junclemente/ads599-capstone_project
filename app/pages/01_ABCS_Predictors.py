#import libraries 
import streamlit as st
import joblib 
import pandas as pd 

from pathlib import Path 



st.set_page_config(page_title="ABCS Predictors", layout="wide")
st.title("ABCS Predictor Inputs")



# set paths - notebooks AND .py scripts
if "__file__" in globals():
    BASE_DIR = Path(__file__).resolve().parent
else:
    BASE_DIR = Path.cwd()


# print(BASE_DIR)
MODEL_PATH = BASE_DIR / "../../models/random_forest_ews.pkl"
FEATURE_PATH = BASE_DIR / "../../models/top_features.pkl"

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


# create 4 columns
col_A, col_B, col_C, col_S = st.columns(4)

# dictionary to hold slider values 
feature_inputs = {}

# A - Attendance
with col_A:
    st.subheader("A: Attendance")
    for feature in attendance_features:
        value = st.slider(
            feature, 
            min_value = 0,
            max_value = 100, 
            value = 50, 
            key=f"A_{feature}",
            label_visibility = "visible"
        )
        feature_inputs[feature] = value 

# B - Behavior / Climate Support 
with col_B:
    st.subheader("B: Behavior")
    for feature in behavior_features:
        value = st.slider(
            feature,
            min_value=0,
            max_value=100,
            value=50,
            key=f"B_{feature}",
            label_visibility="visible"
        )
        feature_inputs[feature] = value

# C — COURSE PERFORMANCE
with col_C:
    st.subheader("C: Course")
    for feature in course_features:
        value = st.slider(
            feature,
            min_value=0,
            max_value=100,
            value=50,
            key=f"C_{feature}",
            label_visibility="visible"
        )
        feature_inputs[feature] = value


# S — SCHOOL / CONTEXT SUPPORTS
with col_S:
    st.subheader("S: Supports")
    for feature in support_features:
        value = st.slider(
            feature,
            min_value=0,
            max_value=100,
            value=50,
            key=f"S_{feature}",
            label_visibility="visible"
        )
        feature_inputs[feature] = value


st.markdown("### Understanding the ABCS Categories")

colA, colB, colC, colS = st.columns(4)

with colA:
    st.subheader("A: Attendance")
    st.markdown(
        """
        Attendance indicators capture how consistently students  
        are present in school. Chronic absenteeism and unexcused  
        absences are among the strongest predictors of dropout risk.
        """
    )

with colB:
    st.subheader("B: Behavior")
    st.markdown(
        """
        Behavior reflects school climate and student engagement.  
        Supports such as counselor availability and administrative  
        leadership shape behavior, belonging, and safety.
        """
    )

with colC:
    st.subheader("C: Course")
    st.markdown(
        """
        Course performance measures student progress toward  
        graduation expectations — including UC/CSU requirements,  
        senior cohort progression, and credit completion.
        """
    )

with colS:
    st.subheader("S: Supports")
    st.markdown(
        """
        School supports represent the resources available to students:  
        experienced teachers, reasonable class sizes, and the  
        socioeconomic context of the school community.
        """
    )

st.divider()
st.header("Feature Input Dictionary")

st.json(feature_inputs)