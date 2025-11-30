import random
import streamlit as st

def randomize_feature_values(features, slider_settings, key_prefix=""):
    """
    Randomizes values for a list of feature names using their slider settings.
    
    Parameters
    ----------
    features : list
        List of feature names to randomize.
    
    slider_settings : dict
        Dictionary containing min, max, default, and label for each feature.
    
    key_prefix : str
        Optional prefix for session_state keys (e.g., "imp_" for importance page).
    """
    for feature in features:
        s = slider_settings.get(feature)

        if s is None:
            continue

        # Continuous (float) or integer?
        if isinstance(s["default"], float):
            value = round(random.uniform(s["min"], s["max"]), 4)
        else:
            value = random.randint(s["min"], s["max"])

        # Update the associated slider key
        st.session_state[key_prefix + feature] = value
