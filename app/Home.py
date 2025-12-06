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

This application accompanies our MS in Applied Data Science capstone project at the University of San Diego.
It demonstrates a school-level Early Warning System (EWS) built entirely from publicly available, FERPA-compliant datasets from the California Department of Education.

The goal of the project is to identify high schools that may be emerging at risk for lower graduation outcomes, using indicators aligned with the established ABC(S) early warning framework:

- **A — Attendance:** chronic absenteeism rates and unexcused absence patterns  
- **B — Behavior:** suspension metrics and school climate indicators (CalSCHLS)  
- **C — Course Performance:** still-enrolled rates and academic progress signals  
- **S — School Context:** staffing, school demographics, and socioeconomic factors (FRPM, county patterns)  

Using these features, we trained a Random Forest classifier to estimate whether a school’s Adjusted Cohort Graduation Rate (ACGR) is likely to fall below 90%, which our project uses as a preventive early-warning threshold, not a judgment of school quality.

This Streamlit app serves as a prototype decision-support tool, allowing users to explore real school data, adjust key indicators, and observe how the model responds—illustrating how publicly available data can generate scalable, privacy-preserving insights for educational leaders.
""")

st.markdown("""
### What does this app do?

This prototype app allows you to interact with our Early Warning System model through four main sections:

#### 1. School Explorer
Select any California public high school—or generate a random one—and instantly view its key indicators (attendance, academic, and demographic inputs) alongside the model’s predicted graduation-risk classification. This section shows how the model behaves using real school data.

#### 2. ABCS by Category
Explore the top predictors grouped into the Early Warning System categories:

- Attendance  
- Behavior  
- Course Performance  
- School Context (S)  

Adjust the sliders to see how changes in each category influence the model’s prediction.

#### 3. ABCS by Feature Importance
View the same top 15 features ranked from most to least important based on the Random Forest model's final feature importances.  
This view highlights which indicators drive predictions the most.

#### 4. Data Dictionary
Browse detailed definitions for every feature used in the model, including source datasets, calculation notes, and how each variable fits into the ABCS framework.
""")

st.divider()

st.header("How the ABC(S) Inputs Work")

left, right = st.columns([1.4, 1.6], vertical_alignment="top")

with right:
    img_path = ASSETS_DIR / "abcs_input_sliders.png"
    st.image(str(img_path), caption="ABC(S) input categories used for prediction", use_container_width=True)

with left:
    st.markdown(
        """
        On the **ABCS by Category** page, you can adjust key indicators grouped into four categories:

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

- Start with **School Explorer** to view real California high school data, see the model’s predicted graduation-risk classification, and adjust key indicators to understand how they influence the outcome.  
- Use **ABCS by Category** to explore the top predictors grouped into the Early Warning System framework (Attendance, Behavior, Course performance, and School context).  
- Visit **ABCS by Feature Importance** to view the same predictors ranked from most to least important in the final Random Forest model.  
- Refer to the **Data Dictionary** for definitions, source notes, and descriptions of all variables included in the system.

> **Note:** This is a research prototype designed for learning and demonstration purposes.  
> It is **not** an official CDE tool and should not be used for high-stakes or operational decision-making.
""")

st.divider()

st.markdown(
    "<p style='text-align:center;'>"
    "🔗 <a href='https://github.com/junclemente/ca-early-warning-system' target='_blank'>Project Repository</a>"
    "</p>",
    unsafe_allow_html=True,
)

