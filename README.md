# 📊 HR Churn Intelligence System — End-to-End Machine Learning Project

### 🔗 Live Deployment  
- **Streamlit Web App:** https://churnpredictionstack.streamlit.app/

---

## 📘 Overview

This project predicts **employee attrition (churn risk)** using structured HR data.

It demonstrates a complete **Machine Learning lifecycle** — from exploratory data analysis and ensemble modeling to deployment using **Flask API** and an interactive **Streamlit Dashboard**.

---

## 🚀 Key Highlights

- 📊 Exploratory Data Analysis (9 Business Insight Plots)
- 🤖 Model Comparison (LR, RF, XGBoost, CatBoost)
- 🧠 Stacked Ensemble Model (Final Production Model)
- 🎯 Threshold Optimization (Business-ready)
- 🌐 Flask REST API Deployment
- 📊 Enterprise-style Streamlit Dashboard

---

# 📊 Dataset Information

| Feature | Description |
|----------|-------------|
| Age | Employee age |
| Department | Business department |
| Designation | Job role |
| Salary_Band | Compensation category |
| Work_Life_Balance | Work-life satisfaction |
| Job_Satisfaction | Job happiness rating |
| Performance_Band | Performance level |
| Travel_Frequency | Business travel frequency |
| OverTime | Overtime status |
| Tenure_Band | Experience band |
| Attrition | 1 = Left, 0 = Stayed |

---

# 📈 Exploratory Data Analysis (EDA)

Performed in `hr_churn_notebook.ipynb`

---

## 1️⃣ Churn Distribution by Gender

![Churn vs Gender](images/churn_vs_gender.png)

**Insight:**  
More male employees are observed in churn cases (relative workforce size should be considered).

---

## 2️⃣ Tenure vs Attrition

![Tenure vs Attrition](images/tenure_vs_attrition.png)

**Insight:**  
Employees within **6–24 months** are most likely to churn.

---

## 3️⃣ Designation & Tenure vs Churn

![Designation Tenure](images/designation_tenure_vs_attrition.png)

**Insight Highlights:**
- Lab Technicians & Sales Reps churn early (0–6 months)
- HR & Sales churn in 6–24 months
- Research Scientists churn in 5–10 years

Retention strategy must be role-specific.

---

## 4️⃣ Performance vs Job Satisfaction vs Churn

![Performance Job Satisfaction](images/performance_job_satisfaction.png)

**Insight:**  
High-performing employees with low job satisfaction show the highest churn risk.

---

## 5️⃣ Performance vs Department

![Performance Department](images/performance_department.png)

**Insight:**  
Sales (mid-performers) and R&D (high-performers) show elevated churn.

---

## 6️⃣ Salary Band vs Attrition

![Salary vs Attrition](images/salary_vs_attrition.png)

**Insight:**  
Low salary employees show the highest churn probability.

---

## 7️⃣ Salary vs Commute Distance vs Churn

![Salary Commute](images/salary_commute_attrition.png)

**Insight:**  
Low salary + long commute = highest churn risk.

---

## 8️⃣ Work-Life Balance vs Travel Frequency

![WLB Travel](images/wlb_travel_attrition.png)

**Insight:**  
Low work-life balance combined with frequent travel significantly increases churn.

---

## 9️⃣ Overtime vs Department vs Churn

![Overtime Department](images/overtime_department_attrition.png)

**Insight:**  
Higher overtime exposure correlates with elevated churn, especially in Sales.

---

# 🤖 Machine Learning Model Comparison

| Model | Accuracy | Precision (Churn) | Recall (Churn) | F1 | ROC-AUC |
|--------|-----------|------------------|----------------|------|---------|
| Logistic Regression | 0.87 | 0.71 | 0.36 | 0.48 | 0.82 |
| Random Forest | 0.84 | 0.50 | 0.11 | 0.18 | 0.79 |
| XGBoost | 0.84 | 0.49 | 0.45 | 0.47 | 0.80 |
| CatBoost | 0.87 | 0.68 | 0.40 | 0.51 | 0.80 |
| 🏆 Stacked Ensemble | **0.89** | **0.74** | **0.49** | **0.59** | **0.83+** |

---

# 🏆 Final Model

### 🥇 Stacked Model @ 0.4 Threshold

- Precision: 0.74  
- Recall: 0.49  
- F1 Score: 0.59  
- Accuracy: 0.89  

Balanced and production-ready performance.

---

# ⚙️ Flask REST API

### Endpoints

| Route | Method | Description |
|--------|---------|-------------|
| `/` | GET | Health check |
| `/predict` | POST | Returns churn probability & risk category |

### Example Response

```json
{
  "churn_probability": 0.62,
  "prediction": "High Risk",
  "threshold_used": 0.4
}
```

---

# 📊 Streamlit Dashboard Features

- Interactive employee profile form
- Risk probability display
- Risk category (Low / Medium / High)
- Clean enterprise UI
- Downloadable risk report

---

# 📦 Project Structure

```
HR-Churn-Intelligence/
│
├── models/
│   ├── stack_model.joblib
│   ├── preprocessor.joblib
│   ├── threshold.json
│   └── feature_schema.json
│
├── images/
│   ├── churn_vs_gender.png
│   ├── tenure_vs_attrition.png
│   ├── designation_tenure_vs_attrition.png
│   ├── performance_job_satisfaction.png
│   ├── performance_department.png
│   ├── salary_vs_attrition.png
│   ├── salary_commute_attrition.png
│   ├── wlb_travel_attrition.png
│   └── overtime_department_attrition.png
│
├── app/
│   └── app.py
│
├── streamlit_app.py
├── hr_churn_notebook.ipynb
├── requirements.txt
└── README.md
```

---

# 📌 Conclusion

This project delivers a production-ready **HR Analytics Intelligence System** capable of identifying high-risk employees using advanced ensemble learning.

The final stacked model provides strong precision while maintaining meaningful recall, making it suitable for strategic workforce retention planning.
