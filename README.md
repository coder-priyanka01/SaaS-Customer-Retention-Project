# 📊 SaaS Customer Retention & Revenue Risk Intelligence System

🔗 **Live Application:**  
https://saas-customer-retention-project.streamlit.app/

---

## 🚀 Project Overview

Customer churn is one of the most critical revenue threats in SaaS businesses. Even a small increase in churn rate can significantly impact recurring revenue and long-term growth.

This project is not just a churn prediction model — it is a Revenue Risk Intelligence System that transforms machine learning outputs into actionable business decisions.

It enables leadership teams to:

. Identify high-risk customers early

. Quantify financial exposure

. Prioritize retention campaigns

. Optimize customer success efforts

. Reduce preventable revenue loss

🎯 Business Problem

In SaaS models:

. Revenue is recurring

. Customer Lifetime Value (CLV) is crucial

. Retention is more cost-effective than acquisition

However, most companies only track churn after it happens.

This system shifts from reactive churn reporting to proactive churn prevention.

---

💡 Business Value Delivered

Instead of showing just churn probability, this application:

✔ Converts churn risk into Revenue at Risk
✔ Segments customers into actionable risk buckets
✔ Helps prioritize high-value at-risk accounts
✔ Supports data-driven retention strategy

This bridges the gap between Data Science and Business Strategy.

---

## 🧠 Machine Learning Workflow

### 1️⃣ Model Development (Notebook)
- Dataset: `SaaS-Sales.csv`
- Model trained in Jupyter/Colab notebook
- XGBoost Classifier used for prediction
- Model saved using `joblib`
- Feature order saved separately (`model_features.pkl`) to ensure prediction consistency

### 2️⃣ Model Deployment
- Model loaded in Streamlit app
- Feature alignment ensured before prediction
- Probability extracted using `predict_proba`
- Revenue impact calculated dynamically

---

📊 Revenue Intelligence Layer

The system calculates:

Revenue at Risk = Sales × Churn Probability

This transforms a technical ML prediction into a financial KPI that executives can immediately interpret.

Example:

. Customer Sales = $10,000

. Churn Probability = 0.70

. Revenue at Risk = $7,000

This makes the model decision-ready

---

## 🖥️ Application Features

### 📊 Executive Dashboard
- Risk distribution visualization (Low / Medium / High)
- Revenue-at-risk calculator
- Business metrics display
- Session-based prediction aggregation

### 🤖 Churn Prediction Engine
- User input for numerical & categorical features
- One-hot encoding alignment
- Probability prediction
- Risk classification thresholds:
  - Low Risk: < 35%
  - Medium Risk: 35–65%
  - High Risk: > 65%
- Revenue-at-risk estimation:
Revenue at Risk = Sales × Churn Probability

---

## 📂 Project Structure
├── app.py
├── churn_model.pkl
├── model_features.pkl
├── SaaS-Sales.csv
├── SaaS_Customer_Retention_&_Revenue_Risk_Intelligence_System.ipynb
├── requirements.txt
├── runtime.txt

---

## 🔧 Technical Stack

- Python 3.11
- Streamlit
- XGBoost
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Joblib

---

## 🏗️ Key Implementation Details

### ✔ Feature Handling
Categorical variables (Region, Subregion, Industry, Segment) are one-hot encoded.  
Feature order is strictly maintained using `model_features.pkl`.

### ✔ Prediction Safety
Before inference:
- Missing features are auto-filled with 0
- Columns reordered to match training schema

This prevents deployment-time feature mismatch errors.

### ✔ Revenue Intelligence Layer
Model output is not just shown as probability.
It is converted into financial exposure to make insights business actionable.

---

## 🚀 Deployment

The app is deployed using Streamlit Cloud.

Dependency management:
- `requirements.txt`
- `runtime.txt` (Python 3.11)

---

📚 Key Learnings

. Translating ML outputs into financial metrics

. Aligning data science with executive KPIs

. Model serialization & production deployment

. Feature consistency management

. Building ML-powered business dashboards

---

## 👩‍💻 Author

**Priyanka**

AI & Data Science Enthusiast  
Focused on building business-driven ML applications.

---

⭐ If you find this project interesting, feel free to star the repository.
