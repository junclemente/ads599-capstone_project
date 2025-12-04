# import libraries 
import streamlit as st
import joblib 
import pandas as pd 

from pathlib import Path 
from utils.paths import get_paths
from utils.feature_config import slider_settings
from utils.randomizer import randomize_feature_values

paths = get_paths()
MODELS_DIR = paths["MODELS_DIR"]

MODEL_PATH = MODELS_DIR / "random_forest_ews.pkl"
FEATURE_PATH = MODELS_DIR / "top_features.pkl"

# load models/features
top_features = joblib.load(FEATURE_PATH)
model = joblib.load(MODEL_PATH)

st.set_page_config(
    page_title="ABCS by Feature Importance",
    page_icon="⭐",
    layout="wide"
)

st.title("⭐ ABCS by Feature Importance")
st.header("Feature Inputs by Order of Importance")

# Filter ordered features to only those with slider settings
ordered_features = [f for f in top_features if f in slider_settings]

# --- Randomize Inputs button ---
col_label, col_btn = st.columns([4, 1])

with col_label:
    st.markdown(
        "Adjust the sliders based on feature importance, or click **Randomize Inputs** to "
        "sample a new combination of values."
    )

with col_btn:
    if st.button("🎲 Randomize Inputs"):
        randomize_feature_values(
            ordered_features,
            slider_settings,
            key_prefix="imp_",    # matches st.slider keys (imp_feature_name)
        )
        st.rerun()

# create 3 columns
col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

# dict to store slider values
feature_values = {}

# Render sliders with randomized or previous values
for i, feature in enumerate(ordered_features):
    col_idx = i // 5
    rank = i + 1
    s = slider_settings[feature]

    with cols[col_idx]:
        st.markdown(f"**{rank}. {s['label']}**")

        value = st.slider(
            "",
            s["min"],
            s["max"],
            value=st.session_state.get(f"imp_{feature}", s["default"]),
            help=s.get("description"),
            key=f"imp_{feature}",
        )

        feature_values[feature] = value


# ----- Model prediction -----

# create dataframe of values
input_df = pd.DataFrame({
    feature: [feature_values[feature]]
    for feature in ordered_features
})

# reorder features according to the model
input_df = input_df.reindex(columns=top_features)

st.divider()

prediction = model.predict(input_df)[0]
risk_label = "At Risk" if prediction == 1 else "On Track"
st.subheader(f"Model Prediction: {risk_label}")

probability = model.predict_proba(input_df)[0][1]
st.write(f"Risk Probability: {round(probability * 100,1)}%")

st.divider()
