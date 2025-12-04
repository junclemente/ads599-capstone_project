#import libraries 
import streamlit as st
import joblib 
import pandas as pd 

from pathlib import Path 
from utils.paths import get_paths
from utils.feature_config import slider_settings

paths = get_paths()
MODELS_DIR = paths["MODELS_DIR"]


# print(BASE_DIR)
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


ordered_features = [f for f in top_features if f in slider_settings]
# ordered_features = ordered_features[:15]

# create 3 columns
col1, col2, col3 = st.columns(3) 
cols = [col1, col2, col3]

# dict to store slider values
feature_values = {}

for i, feature in enumerate(ordered_features): 
    # calculate column index 
    col_idx = i // 5
    # add ranking label to each column
    rank = i + 1 

    with cols[col_idx]:
        s = slider_settings[feature]
        # use markdown to show rank + label
        st.markdown(f"**{rank}. {s['label']}**")

        value = st.slider(
            "", 
            s["min"], 
            s["max"],
            s["default"],
            key=f"imp_{feature}", 
            help=s.get("description") 
        )
        feature_values[feature] = value


# Model prediction 

# create dataframe of values
input_df = pd.DataFrame({
    # feature: [st.session_state[feature]]
    feature: [feature_values[feature]]
    for feature in ordered_features
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
