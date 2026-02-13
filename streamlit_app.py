import streamlit as st
import joblib
import json
import pandas as pd
import os

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title=" Churn Intelligence Dashboard",
    layout="wide",
    page_icon="📊"
)

st.title("📊 Stack_ML Churn Intelligence System")
st.markdown("Enterprise Employee Risk Monitoring System")

# --------------------------------------------------
# LOAD ARTIFACTS
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "stack_model.joblib")
THRESHOLD_PATH = os.path.join(BASE_DIR, "models", "threshold.json")

model = joblib.load(MODEL_PATH)

with open(THRESHOLD_PATH) as f:
    threshold = json.load(f)["threshold"]

# --------------------------------------------------
# SIDEBAR INPUTS
# --------------------------------------------------
st.sidebar.header("Employee Profile Input")

Age = st.sidebar.slider("Age", 18, 60, 30)
Total_Experience_Years = st.sidebar.slider("Total Experience (Years)", 0, 40, 5)
Previous_Companies = st.sidebar.slider("Previous Companies", 0, 10, 1)
Salary_Hike_Percent = st.sidebar.slider("Salary Hike %", 0, 50, 15)
Trainings_Last_Year = st.sidebar.slider("Trainings Last Year", 0, 10, 2)
Years_In_Current_Role = st.sidebar.slider("Years In Current Role", 0, 20, 3)
Years_Since_Last_Promotion = st.sidebar.slider("Years Since Last Promotion", 0, 15, 2)
Years_With_Current_Manager = st.sidebar.slider("Years With Current Manager", 0, 20, 3)

Salary_Band = st.sidebar.selectbox("Salary Band", ["Low", "Medium", "High", "Very High"])
Performance_Band = st.sidebar.selectbox("Performance", ["Low", "Medium", "High"])
Work_Life_Balance = st.sidebar.selectbox("Work Life Balance", ["Low", "Medium", "High", "Very High"])
Environment_Satisfaction = st.sidebar.selectbox("Environment Satisfaction", ["Low", "Medium", "High", "Very High"])
Job_Satisfaction = st.sidebar.selectbox("Job Satisfaction", ["Low", "Medium", "High", "Very High"])
Relationship_Satisfaction = st.sidebar.selectbox("Relationship Satisfaction", ["Low", "Medium", "High", "Very High"])
Travel_Frequency = st.sidebar.selectbox("Travel Frequency", ["Non-Travel", "Rarely", "Frequently"])
Tenure_Band = st.sidebar.selectbox("Tenure Band", ["0-6m", "6-24m", "2-5y", "5-10y", "10y+"])
Department = st.sidebar.selectbox("Department", ["Sales", "HR", "IT", "Finance"])
Education_Field = st.sidebar.selectbox("Education Field", ["Life Sciences", "Medical", "Technical", "Other"])
Marital_Status = st.sidebar.selectbox("Marital Status", ["Single", "Married", "Divorced"])
Designation = st.sidebar.selectbox("Designation", ["Level_1", "Level_2", "Level_3"])
Commute_Band = st.sidebar.selectbox("Commute Band", ["Short", "Medium", "Long"])
JobInvolvement = st.sidebar.selectbox("Job Involvement", ["Low", "Medium", "High", "Very High"])

Gender = st.sidebar.selectbox("Gender", [0, 1])
OverTime = st.sidebar.selectbox("OverTime", [0, 1])

# --------------------------------------------------
# CREATE INPUT DATAFRAME
# --------------------------------------------------
input_df = pd.DataFrame([{
    "Age": Age,
    "Total_Experience_Years": Total_Experience_Years,
    "Previous_Companies": Previous_Companies,
    "Salary_Hike_Percent": Salary_Hike_Percent,
    "Trainings_Last_Year": Trainings_Last_Year,
    "Years_In_Current_Role": Years_In_Current_Role,
    "Years_Since_Last_Promotion": Years_Since_Last_Promotion,
    "Years_With_Current_Manager": Years_With_Current_Manager,
    "Salary_Band": Salary_Band,
    "Performance_Band": Performance_Band,
    "Work_Life_Balance": Work_Life_Balance,
    "Environment_Satisfaction": Environment_Satisfaction,
    "Job_Satisfaction": Job_Satisfaction,
    "Relationship_Satisfaction": Relationship_Satisfaction,
    "Travel_Frequency": Travel_Frequency,
    "Tenure_Band": Tenure_Band,
    "Department": Department,
    "Education_Field": Education_Field,
    "Marital_Status": Marital_Status,
    "Designation": Designation,
    "Commute_Band": Commute_Band,
    "JobInvolvement": JobInvolvement,
    "Gender": Gender,
    "OverTime": OverTime
}])

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------
if st.button("🔍 Predict Churn Risk"):

    probability = model.predict_proba(input_df)[0][1]
    prediction = int(probability >= threshold)

    st.subheader("Prediction Result")

    st.metric("Churn Probability", f"{probability:.2f}")
    st.metric("Prediction", "High Risk" if prediction == 1 else "Low Risk")

    st.progress(float(probability))

