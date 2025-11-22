# import libraries 
import streamlit as st

from utils.paths import get_paths

paths = get_paths()
ASSETS_DIR = paths["ASSETS_DIR"]

st.set_page_config(page_title="California EWS", page_icon="🎓", layout="wide")


# header
st.title("🎓 California Early Warning System (EWS)")
st.subheader("Capstone Project — Prototype Web App")

st.write(
    """
    Welcome to the prototype of our **Early Warning System** model fo California public high schools. 
    This tool uses statewide indicators aligned to the **ABC framework** — **Attendance**, **Behavior/Climate**, and  
    **Course Performance** — to identify schools at risk of low graduation outcomes.
    """
)         

        
st.markdown("### What this app lets you do")
st.markdown(
    """
    - **Explore** school-level indicators across California  
    - **Enter ABC-aligned inputs** and generate a graduation-risk prediction  
    - **View model insights**, including key predictors and feature importance  
    - **Support decision-making** by highlighting where targeted interventions may help most  
    """
)

st.divider() 

st.header("How the ABCS Inputs Work")

left, right = st.columns([1.4, 1.6], vertical_alignment="top")

with right:
    img_path = ASSETS_DIR /"abcs_input_sliders.png"
    st.image(str(img_path), caption="ABCS input categories used for prediction", width="stretch")

with left:
    st.markdown(
        """
        On the **ABCS Predictor** page, you can adjust key indicators grouped into four categories:

        **A — Attendance**  
        Measures student presence and persistence (e.g., chronic absenteeism, enrollment).

        **B — Behavior / Climate Supports**  
        Captures support structures linked to engagement and safety (e.g., counselor/admin ratios).

        **C — Course Performance**  
        Represents academic progress toward graduation and UC/CSU readiness.

        **S — School Supports & Context**  
        Reflects resource and demographic context that shapes learning conditions.
        
        After entering values, the model returns a predicted graduation-risk classification and
        highlights which inputs are most influential.
        """
    )

st.divider()
st.markdown("➡️ Use the sidebar to open **ABCS Predictor** and try the full model.")

st.info(
    "This is an early prototype for demonstration and evaluation. "
    "Final features and visualizations will be added as modeling is finalized."
)

# Placeholder for upcoming sections
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

