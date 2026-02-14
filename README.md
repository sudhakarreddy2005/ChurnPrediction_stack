# 📊 HR Churn Intelligence System — End-to-End Machine Learning Project

### 🔗 Live Deployments    
- **Streamlit Web App:** https://churnpredictionstack.streamlit.app/ 

---

## 📘 Overview

This project predicts **employee attrition (churn risk)** using structured HR workforce data.

It demonstrates a complete **Machine Learning lifecycle** — from data analysis and advanced ensemble modeling to deployment using **Flask REST API** and an interactive **Streamlit dashboard**.

---

### 🚀 Key Highlights

- 📊 Deep Exploratory Data Analysis (EDA)
- 🤖 Comparative Model Evaluation (LR, RF, XGBoost, CatBoost)
- 🧠 Stacked Ensemble Model (Final Production Model)
- 🎯 Threshold Optimization for Business Needs
- 🌐 Production-ready Flask API
- 📊 Enterprise-grade Streamlit Dashboard
- 🚀 Deployment on Render & Streamlit Cloud

---

# 📊 Dataset Information

The dataset contains employee-level HR attributes used to predict attrition.

| Feature | Description |
|----------|-------------|
| Age | Employee age |
| Department | Business department |
| Designation | Job role |
| Salary_Band | Compensation category |
| Work_Life_Balance | Work-life satisfaction level |
| Job_Satisfaction | Job happiness rating |
| Environment_Satisfaction | Workplace satisfaction |
| Relationship_Satisfaction | Peer relationship rating |
| Performance_Band | Performance evaluation |
| Travel_Frequency | Business travel frequency |
| OverTime | Overtime status |
| Tenure_Band | Experience band |
| Years_With_Current_Manager | Reporting duration |
| Attrition | 1 = Left Company, 0 = Stayed |

---

# 📈 Exploratory Data Analysis (EDA)

Performed in `hr_churn_notebook.ipynb`

---

### 1️⃣ Salary Band vs Attrition
![Salary vs Attrition](images/salary_vs_attrition.png)

> 💬 **Insight:**  
Low salary band employees show significantly higher churn probability.

---

### 2️⃣ Work-Life Balance vs Attrition
![Work Life Balance](images/wlb_vs_attrition.png)

> 💬 **Insight:**  
Low work-life balance strongly correlates with attrition.

---

### 3️⃣ Job Satisfaction vs Attrition
![Job Satisfaction](images/job_satisfaction_vs_attrition.png)

> 💬 **Insight:**  
Low job satisfaction is one of the strongest churn indicators.

---

### 4️⃣ Travel Frequency vs Attrition
![Travel Frequency](images/travel_vs_attrition.png)

> 💬 **Insight:**  
Frequent business travel increases attrition probability.

---

### 5️⃣ Tenure Band vs Attrition
![Tenure Band](images/tenure_vs_attrition.png)

> 💬 **Insight:**  
Early-tenure employees show higher churn risk.

---

### 6️⃣ Overtime vs Attrition
![Overtime](images/overtime_vs_attrition.png)

> 💬 **Insight:**  
Overtime employees have elevated attrition levels.

---

### 7️⃣ Performance Band vs Attrition
![Performance Band](images/performance_vs_attrition.png)

> 💬 **Insight:**  
High performers with dissatisfaction leave faster.

---

### 8️⃣ Department-wise Attrition
![Department](images/department_vs_attrition.png)

> 💬 **Insight:**  
Sales department exhibits the highest churn rate.

---

# 🤖 Machine Learning Model Comparison

| Model | Accuracy | Precision (Churn) | Recall (Churn) | F1 | ROC-AUC |
|--------|-----------|------------------|----------------|------|---------|
| Logistic Regression | 0.87 | 0.71 | 0.36 | 0.48 | 0.82 |
| Random Forest | 0.84 | 0.50 | 0.11 | 0.18 | 0.79 |
| XGBoost | 0.84 | 0.49 | 0.45 | 0.47 | 0.80 |
| CatBoost | 0.87 | 0.68 | 0.40 | 0.51 | 0.80 |
| 🏆 Stacked Ensemble (Final) | **0.89** | **0.74** | **0.49** | **0.59** | **0.83+** |

---

# 🏆 Final Model Selection

### 🥇 Stacked Model @ 0.4 Threshold

- Precision (Churn): 0.74  
- Recall (Churn): 0.49  
- F1 Score: 0.59  
- Accuracy: 0.89  

Balanced and business-ready performance.

---

# ⚙️ Flask REST API — `app.py`

### Endpoints

| Route | Method | Description |
|--------|---------|-------------|
| `/` | GET | Health check |
| `/predict` | POST | Returns churn probability and risk category |

### Example Request

```json
{
  "Age": 35,
  "Department": "Sales",
  "Salary_Band": "Low",
  "Work_Life_Balance": "Low",
  "Job_Satisfaction": "Low",
  "Travel_Frequency": "Frequently",
  "OverTime": 1
}
```

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
- Risk probability meter
- Risk category (Low / Medium / High)
- Enterprise-style UI


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
│   ├── salary_vs_attrition.png
│   ├── wlb_vs_attrition.png
│   ├── job_satisfaction_vs_attrition.png
│   ├── travel_vs_attrition.png
│   ├── tenure_vs_attrition.png
│   ├── overtime_vs_attrition.png
│   ├── performance_vs_attrition.png
│   └── department_vs_attrition.png
│
├── app/
│   └── app.py
│
├── streamlit_app.py
│
├── notebookd/
│    └──  churn_notebook.ipynb

├── requirements.txt
└── README.md
```

---

# 🧠 Skills Demonstrated

- Feature Engineering
- Ensemble Learning & Stacking
- Cross Validation & Hyperparameter Tuning
- Threshold Optimization
- API Development (Flask)
- Dashboard Development (Streamlit)

---

# 📌 Conclusion

This project demonstrates a production-ready **HR Analytics System** capable of identifying high-risk employees using advanced ensemble machine learning.

The final stacked model delivers strong precision while maintaining meaningful recall, making it suitable for real-world workforce monitoring and retention planning.
