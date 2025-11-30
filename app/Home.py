# import libraries 
import streamlit as st

from utils.paths import get_paths

paths = get_paths()
ASSETS_DIR = paths["ASSETS_DIR"]

st.set_page_config(page_title="California EWS", page_icon="🎓", layout="wide")


# header
st.title("🎓 California High School Early Warning System (EWS) Prototype")

st.subheader("Project Introduction and Objective")
st.markdown("""

### What is this project?

This app is part of our MS in Applied Data Science capstone at the University of San Diego.  
We built a **school-level Early Warning System (EWS)** that uses publicly available California 
Department of Education data to flag high schools that may be **at risk of lower graduation rates**.

Our model combines indicators aligned with the **ABC framework**:

- **A – Attendance:** chronic absenteeism and unexcused absences  
- **B – Behavior:** suspensions and school safety / climate indicators  
- **C – Course performance:** delayed completion and still-enrolled rates  
- **S – School context:** demographics, staffing, and socio-economic indicators  

The target outcome is whether a school’s **Adjusted Cohort Graduation Rate (ACGR)** falls below 90%, 
which we use as an **early warning threshold** rather than a measure of failure.
""")         

        
st.markdown("""
### What does this app do?

This prototype app allows you to:

1. **Explore the top 15 predictive features** our model found most useful for distinguishing  
   “On Track” vs “At Risk” high schools.
2. View these features in two ways:
   - **By ABC(S) category** – see which indicators fall under Attendance, Behavior, Course, or School context.
   - **By overall importance** – ranked from most to least important in the final model.

In our full workflow, these features feed into a machine learning model that outputs the probability 
that a school is **“At Risk” of graduating fewer than 90% of its students.**
""")

st.divider()




st.header("How the ABC(S) Inputs Work")

left, right = st.columns([1.4, 1.6], vertical_alignment="top")

with right:
    img_path = ASSETS_DIR /"abcs_input_sliders.png"
    st.image(str(img_path), caption="ABC(S) input categories used for prediction", width="stretch")

with left:
    st.markdown(
        """
        On the **ABC(S) Predictor** page, you can adjust key indicators grouped into four categories:

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

st.markdown("""
### How to use this app

- Go to **“Top 15 Features by ABCS”** to explore indicators grouped by Attendance, Behavior, Course performance, and School context.  
- Go to **“Top 15 Features by Importance”** to see how the model ranks these indicators overall.

> **Note:** This is a research prototype for learning and demonstration.  
> It is **not** an official CDE early warning system and should not be used for high-stakes decisions.
""")

st.divider()

st.markdown("➡️ Use the sidebar to open **ABCS Predictor** and try the full model.")
