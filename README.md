# 📊 SaaS Customer Retention & Revenue Risk Intelligence System


🔗 **Live Application**  
https://saas-customer-retention-project.streamlit.app/

---

## 🚀 Project Overview

Customer churn is one of the biggest revenue threats in SaaS businesses.  
Even small increases in churn can significantly impact recurring revenue and long-term growth.

This project goes beyond churn prediction.  
It builds a **Revenue Risk Intelligence System** that connects Machine Learning, SQL data modeling, and dashboard analytics to support proactive retention strategy.

The system enables businesses to:

- Identify high-risk customers early  
- Quantify potential revenue loss  
- Segment customers by actionable risk levels  
- Support data-driven retention decisions  

---

## 🏗 System Architecture

1. **Data Layer**
   - Raw SaaS transactional data collected from CSV
   
   - Data cleaning and standardization performed in MySQL

2. **Machine Learning Layer**
   - XGBoost model predicts churn probability
   
   - Model serialized and deployed via Streamlit

3. **Revenue Intelligence Layer**
   - Revenue at Risk = Sales × Churn Probability
   
   - Customers segmented into actionable risk categories

4. **Analytics & Visualization Layer**
   - SQL queries prepare analytical datasets
   
   - Power BI dashboard visualizes churn, revenue risk, and trends

This architecture connects Data Science, Database Engineering, and Business Intelligence into one unified system.

---

## 🎯 Business Problem

In SaaS models:

- Revenue is recurring  

- Customer Lifetime Value (CLV) is critical  

- Retention is more cost-effective than acquisition  

Most companies measure churn after it happens.  
This project shifts from **reactive reporting** to **proactive churn prevention**.

---

## 🧠 Machine Learning Layer

- Dataset: `SaaS-Sales.csv`
- Model: XGBoost Classifier
- Framework: Scikit-learn
- Model serialized using `joblib`
- Feature order preserved using `model_features.pkl`
- Churn probability generated using `predict_proba`

The output of the model is not just a prediction — it feeds the revenue intelligence layer.

---

## 🗄 SQL & Data Layer

- Raw and cleaned SaaS datasets structured in MySQL  
- Date standardization and data cleaning performed  
- Revenue, churn, and risk calculations implemented  
- Indexing applied for performance optimization  
- Year-wise revenue and churn analysis supported  

This layer prepares the dataset for dashboard reporting and business insights.

---

## 📊 Revenue Intelligence Logic

**Revenue at Risk = Sales × Churn Probability**

Example:

- Sales = $10,000  
- Churn Probability = 70%  
- Revenue at Risk = $7,000  

This converts ML output into a financial KPI that executives can act on.

---

## 📈 Power BI Dashboard

The interactive dashboard provides:

- Overall churn rate  
- Revenue at Risk summary  
- High / Medium / Low risk segmentation  
- Industry-wise churn analysis  
- Monthly churn trends  
- Revenue vs churn probability insights  

---

## 🖥️ Streamlit Application

- Real-time churn prediction
- Automatic feature alignment before inference
- Risk classification:
  - Low Risk: < 35%
  - Medium Risk: 35–65%
  - High Risk: > 65%
- Dynamic revenue-at-risk calculation

---

## 🛠 Tech Stack

**Python | Scikit-learn | XGBoost | Pandas | NumPy | MySQL | Power BI | Streamlit**

---

## 📚 Key Learnings

- Translating ML predictions into financial metrics  
- Aligning data science with executive KPIs  
- Database modeling and data standardization  
- Model deployment and feature consistency management  
- Building business-focused ML dashboards  

---

## 👩‍💻 Author

Priyanka  
AI & Data Science Enthusiast  
Focused on building business-driven ML applications.

⭐ If you find this project useful, feel free to star the repository.

⭐ If you find this project interesting, feel free to star the repository.
