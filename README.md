# 📊 SaaS Customer Retention & Revenue Risk Intelligence System

🔗 **Live Application:**  
https://saas-customer-retention-project.streamlit.app/

---

## 🚀 Project Overview

This project is an end-to-end Machine Learning application designed to predict customer churn risk and estimate potential revenue exposure for SaaS businesses.

The system converts predictive model outputs into business-ready insights using an interactive Streamlit dashboard.

---

## 🎯 Objective

To build a deployable ML-powered system that:

- Predicts customer churn probability
- Classifies customers into risk categories
- Calculates revenue-at-risk
- Visualizes risk distribution for business decision-makers

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

## 📂 Project Structure
├── app.py

├── churn_model.pkl

├── model_features.pkl

├── SaaS-Sales.csv

├── SaaS_Customer_Retention_&_Revenue_Risk_Intelligence_System.ipynb

├── requirements.txt

├── runtime.txt

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

## 📈 What Makes This Project Production-Ready?

- End-to-end ML pipeline
- Model serialization
- Feature schema preservation
- Business-focused output transformation
- UI styling and dashboard presentation
- Clean dependency management

---

## 📚 Learning Outcomes

- End-to-end ML deployment workflow
- Handling feature consistency during inference
- Converting ML outputs into business metrics
- Building interactive ML dashboards
- Debugging version & deployment conflicts

---

## 👩‍💻 Author

**Priyanka**

AI & Data Science Enthusiast  
Focused on building business-driven ML applications.

---

⭐ If you find this project interesting, feel free to star the repository.
