# import libraries 
import streamlit as st
import joblib 
import pandas as pd 

from utils.paths import get_paths
from utils.feature_config import (
    attendance_features, 
    behavior_features, 
    course_features,
    support_features, 
    slider_settings,
)
from utils.randomizer import randomize_feature_values

paths = get_paths()
MODELS_DIR = paths["MODELS_DIR"]

MODEL_PATH = MODELS_DIR / "random_forest_ews.pkl"
FEATURE_PATH = MODELS_DIR / "top_features.pkl"

# load models/features
top_features = joblib.load(FEATURE_PATH)
model = joblib.load(MODEL_PATH)

st.set_page_config(
    page_title="ABCS by Category",
    page_icon="📊",
    layout="wide",
)

st.title("📊 ABCS by Category")
st.header("Feature Inputs by ABCS Category")

# All features on this page (for randomizer + model input)
all_features = (
    attendance_features
    + behavior_features
    + course_features
    + support_features
)

# --- Randomize Inputs button ---
col_label, col_btn = st.columns([4, 1])

with col_label:
    st.markdown(
        "Adjust the ABCS sliders to explore different scenarios, "
        "or click **Randomize Inputs** to sample a new combination."
    )

with col_btn:
    if st.button("🎲 Randomize Inputs"):
        # keys for sliders are just the feature names (no prefix)
        randomize_feature_values(
            all_features,
            slider_settings,
            key_prefix="",   # randomizer will write to st.session_state[feature]
        )
        st.rerun()

# dictionary to hold slider values for model input
feature_inputs = {}

# create 4 columns
col_A, col_B, col_C, col_S = st.columns(4)

# A - Attendance
with col_A:
    st.subheader("A: Attendance")
    for feature in attendance_features:
        s = slider_settings[feature]
        value = st.slider(
            s["label"],
            s["min"],
            s["max"],
            # use randomized or previous value if present, otherwise default
            value=st.session_state.get(feature, s["default"]),
            help=s.get("description"),
            key=feature,
        )
        feature_inputs[feature] = value

# B - Behavior / Climate Support 
with col_B:
    st.subheader("B: Behavior")
    for feature in behavior_features:
        s = slider_settings[feature]
        value = st.slider(
            s["label"],
            s["min"],
            s["max"],
            value=st.session_state.get(feature, s["default"]),
            help=s.get("description"),
            key=feature,
        )
        feature_inputs[feature] = value

# C — Course Performance
with col_C:
    st.subheader("C: Course")
    for feature in course_features:
        s = slider_settings[feature]
        value = st.slider(
            s["label"],
            s["min"],
            s["max"],
            value=st.session_state.get(feature, s["default"]),
            help=s.get("description"),
            key=feature,
        )
        feature_inputs[feature] = value

# S — School / Context Supports
with col_S:
    st.subheader("S: Supports")
    for feature in support_features:
        s = slider_settings[feature]
        value = st.slider(
            s["label"],
            s["min"],
            s["max"],
            value=st.session_state.get(feature, s["default"]),
            help=s.get("description"),
            key=feature,
        )
        feature_inputs[feature] = value

# ----- Model prediction -----

# create dataframe of values in correct order
input_df = pd.DataFrame({
    feature: [feature_inputs[feature]]
    for feature in all_features
})

# reorder feature values to match top_features and as expected by model
input_df = input_df.reindex(columns=top_features)

st.divider()

prediction = model.predict(input_df)[0]
risk_label = "At Risk" if prediction == 1 else "On Track"
st.subheader(f"Model Prediction: {risk_label}")

probability = model.predict_proba(input_df)[0][1]
st.write(f"Risk Probability: {round(probability * 100, 1)}%")

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
        Course performance measures student progress toward graduation expectations — including UC/CSU requirements, 
        senior cohort progression, and credit completion.
        """
    )

with colS:
    st.subheader("S: Supports")
    st.markdown(
        """
        School supports represent the resources available to students: experienced teachers, reasonable class sizes, 
        and the socioeconomic context of the school community.
        """
    )
