import streamlit as st 
import pandas as pd 
import joblib 
import random 

from utils.paths import get_paths 
from utils.feature_config import (
    slider_settings, 
    attendance_features, 
    behavior_features, 
    course_features, 
    support_features, 
    get_slider_step
)
from utils.randomizer import randomize_feature_values

paths = get_paths()
MODELS_DIR = paths["MODELS_DIR"]
DATA_DIR = paths["DATA_DIR"]

MODEL_PATH = MODELS_DIR / "random_forest_ews.pkl"
FINAL_DATASET_PATH = DATA_DIR / "06_top15_features_w_ids_and_target.pkl"

model = joblib.load(MODEL_PATH)
df_full = pd.read_pickle(FINAL_DATASET_PATH)

# Top 15 features (model importance order)
TOP_FEATURES = joblib.load(MODELS_DIR / "top_features.pkl")

st.title("School Explorer")

st.markdown("""
Select a California high school to see model prediction, compare them to the actual graduation outcome, and adjust inputs interactively.             
""")
school_list = df_full["school"].sort_values().unique().tolist()

selected_school = st.selectbox("Select a School:", school_list)

school_row = df_full[df_full["school"] == selected_school].iloc[0]



# Create the ordered feature set
ordered_features = [f for f in TOP_FEATURES if f in slider_settings]

# Set sliders based on selected school
for feature in ordered_features:
    key = f"school_{feature}"
    if key not in st.session_state:
        st.session_state[key] = school_row[feature]


colA, colB = st.columns(2)

with colA:
    if st.button("🔀 Random School"):
        random_school = df_full.sample(1).iloc[0]
        for feature in ordered_features:
            st.session_state[f"school_{feature}"] = random_school[feature]
        st.rerun()

with colB:
    if st.button("🎲 Randomize Inputs"):
        randomize_feature_values(
            ordered_features, slider_settings, key_prefix="school_"
        )
        st.rerun()


st.subheader("Feature Inputs")

col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

feature_values = {}

for i, feature in enumerate(ordered_features):
    col_idx = i // 5
    s = slider_settings[feature]
    rank = i + 1

    with cols[col_idx]:
        st.markdown(f"**{rank}. {s['label']}**")

        # Ensure the slider value type matches slider_settings default type
        if isinstance(s["default"], float):
            current_value = float(st.session_state[f"school_{feature}"])
        else:
            current_value = int(st.session_state[f"school_{feature}"])

        value = st.slider(
            "",
            s["min"],
            s["max"],
            current_value,
            step=get_slider_step(feature),
            key=f"school_{feature}",
            help=s.get("description"),
        )
        
        feature_values[feature] = value