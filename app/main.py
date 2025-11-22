# import libraries 
import streamlit as st
import joblib 
import pandas as pd 

from pathlib import Path 

# set paths 
BASE_DIR = Path(__file__).resolve().parent 

print(BASE_DIR)
MODEL_PATH = BASE_DIR / "../models/random_forest_ews.pkl"
FEATURE_PATH = BASE_DIR / "../models/top_features.pkl"

# load models/features
model = joblib.load(MODEL_PATH)
top_features = joblib.load(FEATURE_PATH)


# ----------------------------------------------------
# Streamlit App Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="California EWS Prototype",
    page_icon="🎓",
    layout="wide"
)

# ----------------------------------------------------
# App Header
# ----------------------------------------------------
st.title("🎓 California Early Warning System (EWS)")
st.subheader("Capstone Project — Prototype Web App")

st.write("""
Welcome to the prototype interface for our **Early Warning System** model.  
This app will eventually allow users to:

- Explore school-level data  
- View model-driven insights  
- Predict graduation outcomes  
- Understand risk indicators aligned to the ABC framework  

For now, this is a simple starter page to verify the app structure and deployment environment.
""")

# ----------------------------------------------------
# Top Features
# ----------------------------------------------------

st.subheader("Top Features Used by Model")
st.write(top_features)

# ----------------------------------------------------
# Demo Section
# ----------------------------------------------------
st.header("Quick Demo Section")

st.write("Here is a sample interactive widget:")

user_input = st.slider("Pick a number:", 0, 100, 50)
st.success(f"You selected: **{user_input}**")

# ----------------------------------------------------
# Placeholder for upcoming sections
# ----------------------------------------------------
st.divider()
st.header("Coming Soon")
st.info("""
🔧 **Upcoming features we will add next:**

- Load the final XGBoost model  
- School-level prediction form (FRPM, absenteeism, safety scores, etc.)  
- Data explorer dashboard  
- Feature importance visualizations  
- County or district lookup tools  
""")

