import streamlit as st 
import pandas as pd 
import joblib 

from utils.paths import get_paths 
from utils.feature_config import (
    slider_settings, 
    get_slider_step,
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

# ----------------- MUST DEFINE THIS EARLY -----------------
ordered_features = [f for f in TOP_FEATURES if f in slider_settings]
# -----------------------------------------------------------

st.title("School Explorer")

st.markdown("""
Select a California high school to see model predictions, compare them to 
the actual graduation outcome, and adjust inputs interactively.
""")

# ---------------------------------------------------------------------
# School list + initial state
# ---------------------------------------------------------------------
school_list = df_full["school"].sort_values().unique().tolist()

# Initialize the school selector ONCE
if "school_selector" not in st.session_state:
    st.session_state["school_selector"] = school_list[0]

# Track last selected school for slider initialization
if "last_selected_school" not in st.session_state:
    st.session_state["last_selected_school"] = st.session_state["school_selector"]

# ---------------------------------------------------------------------
# BUTTONS FIRST (modify session_state BEFORE widgets are created)
# ---------------------------------------------------------------------
colA, colB = st.columns(2)

with colA:
    if st.button("🔀 Random School"):
        random_school = df_full.sample(1).iloc[0]
        st.session_state["school_selector"] = random_school["school"]
        # st.session_state["last_selected_school"] = random_school["school"]
        st.rerun()

with colB:
    if st.button("🎲 Randomize Inputs"):
        st.session_state["randomize_inputs"] = True
        st.rerun()

# ---------------------------------------------------------------------
# Now create the selectbox using the updated state
# ---------------------------------------------------------------------
selected_school = st.selectbox(
    "Select a School:",
    school_list,
    key="school_selector",
)

school_row = df_full[df_full["school"] == selected_school].iloc[0]

# ---------------------------------------------------------------------
# If user selected a different school, reset slider defaults
# ---------------------------------------------------------------------
if st.session_state["last_selected_school"] != selected_school:
    for feature in ordered_features:
        key = f"school_{feature}"
        base_val = school_row[feature]
        if isinstance(slider_settings[feature]["default"], float):
            st.session_state[key] = float(base_val)
        else:
            st.session_state[key] = int(base_val)
    st.session_state["last_selected_school"] = selected_school

# ---------------------------------------------------------------------
# Handle "Randomize Inputs" after rerun
# ---------------------------------------------------------------------
if st.session_state.get("randomize_inputs", False):
    randomize_feature_values(
        ordered_features,
        slider_settings,
        key_prefix="school_",
    )
    st.session_state["randomize_inputs"] = False



# ---------------------------------------------------------------------
# Sliders
# ---------------------------------------------------------------------
st.subheader("Feature Inputs")

col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

feature_values = {}

for i, feature in enumerate(ordered_features):
    col_idx = i // 5
    s = slider_settings[feature]
    rank = i + 1
    key = f"school_{feature}"

    with cols[col_idx]:
        st.markdown(f"**{rank}. {s['label']}**")

        value = st.slider(
            "",
            min_value=s["min"],
            max_value=s["max"],
            step=get_slider_step(feature),
            key=key,          # value comes from st.session_state[key]
            help=s.get("description"),
        )

        feature_values[feature] = value

# ---------------------------------------------------------------------
# Model prediction
# ---------------------------------------------------------------------
# # Build input in the exact order the model expects
# features_for_model = [f for f in TOP_FEATURES if f in feature_values]

# input_df = pd.DataFrame(
#     [[feature_values[f] for f in features_for_model]],
#     columns=features_for_model,
# )

# st.divider()

# prediction = model.predict(input_df)[0]
# risk_label = "At Risk" if prediction == 1 else "On Track"
# st.subheader(f"Model Prediction: {risk_label}")

# probability = model.predict_proba(input_df)[0][1]
# st.write(f"Risk Probability: {round(probability * 100, 1)}%")

# st.divider()

# ---------------- Model prediction ----------------

# Build input in the exact order the model expects
features_for_model = [f for f in TOP_FEATURES if f in feature_values]

input_df = pd.DataFrame(
    [[feature_values[f] for f in features_for_model]],
    columns=features_for_model,
)

st.divider()

# Model prediction
prediction = model.predict(input_df)[0]
probability = model.predict_proba(input_df)[0][1]
risk_label = "At Risk" if prediction == 1 else "On Track"

# ---- Actual outcome from dataset ----
TARGET_COL = "low_grad_rate"  # 👈 update this if your target col is named differently
actual_value = school_row[TARGET_COL]
actual_label = "At Risk" if actual_value == 1 else "On Track"

# Display side-by-side
col_pred, col_actual = st.columns(2)

with col_pred:
    st.subheader("Model Prediction")
    st.metric("Status", risk_label)
    st.write(f"Risk Probability: {round(probability * 100, 1)}%")

with col_actual:
    st.subheader("Actual Outcome")
    st.metric("Status", actual_label)

# Optional: highlight match / mismatch
if risk_label == actual_label:
    st.success("✅ Model prediction matches the actual outcome for this school.")
else:
    st.error("❌ Model prediction does NOT match the actual outcome for this school.")

st.divider()
