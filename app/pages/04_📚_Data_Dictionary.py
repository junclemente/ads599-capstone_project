import streamlit as st
import pandas as pd
from utils.feature_config import slider_settings

st.set_page_config(
    page_title="Data Dictionary",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Data Dictionary")

df = pd.DataFrame([
    {
        "Feature": name,
        "Label": cfg["label"],
        "Description": cfg.get("description", "")
    }
    for name, cfg in slider_settings.items()
])

st.dataframe(df, use_container_width=True, height=700)
