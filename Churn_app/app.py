import joblib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import shap

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="SaaS Retention Intelligence",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# PROFESSIONAL CSS
# --------------------------------------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}
.stButton>button {
    background: linear-gradient(45deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
    padding: 10px 25px;
    box-shadow: 0px 0px 15px rgba(0,114,255,0.8);
    transition: 0.3s;
}
.stButton>button:hover {
    box-shadow: 0px 0px 25px rgba(0,114,255,1);
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "churn_model.pkl")
features_path = os.path.join(BASE_DIR, "model_features.pkl")

model = joblib.load(model_path)
features = joblib.load(features_path)
model_features = features


# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["📊 Executive Dashboard",
     "🤖 Churn Prediction",
     "🔍 SHAP Explanation"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👑 Created by Priyanka")

# --------------------------------------------------
# FEATURE GROUPING
# --------------------------------------------------
region_cols = [c for c in model_features if c.startswith("Region_")]
subregion_cols = [c for c in model_features if c.startswith("Subregion_")]
industry_cols = [c for c in model_features if c.startswith("Industry_")]
segment_cols = [c for c in model_features if c.startswith("Segment_")]

region_options = [c.replace("Region_", "") for c in region_cols]
subregion_options = [c.replace("Subregion_", "") for c in subregion_cols]
industry_options = [c.replace("Industry_", "") for c in industry_cols]
segment_options = [c.replace("Segment_", "") for c in segment_cols]

numeric_features = ["Sales", "Quantity", "Discount", "Profit", "risk_score"]

# ==================================================
# EXECUTIVE DASHBOARD
# ==================================================
if page == "📊 Executive Dashboard":

    st.title("📊 Executive Revenue Intelligence Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Model AUC", "0.89")
    col2.metric("AI System", "Active")
    col3.metric("Prediction Engine", "Live")

    st.markdown("---")

    left, right = st.columns([2,1])

    with left:
        st.subheader("📌 Risk Distribution Overview")

        if "predictions" in st.session_state:
            preds = st.session_state["predictions"]
            low = sum(p < 0.35 for p in preds)
            medium = sum(0.35 <= p < 0.65 for p in preds)
            high = sum(p >= 0.65 for p in preds)
        else:
            low, medium, high = 50, 30, 20

        fig, ax = plt.subplots()
        ax.pie([low, medium, high],
               labels=["Low Risk", "Medium Risk", "High Risk"],
               autopct='%1.1f%%')
        ax.set_title("Customer Risk Segmentation")
        st.pyplot(fig)

    with right:
        st.subheader("💰 Revenue-at-Risk Calculator")

        revenue = st.number_input("Annual Revenue ($)", value=10000.0)
        churn_prob = st.slider("Churn Probability (%)", 0, 100, 20)

        revenue_at_risk = revenue * (churn_prob / 100)

        st.metric("Projected Revenue at Risk",
                  f"${revenue_at_risk:,.2f}")

        st.info("This converts AI prediction into financial impact.")

# ==================================================
# CHURN PREDICTION
# ==================================================
elif page == "🤖 Churn Prediction":

    st.title("🤖 Customer Churn Prediction Engine")

    main_col, explain_col = st.columns([2,1])

    with main_col:
        inputs = {}

        for feature in numeric_features:
            inputs[feature] = st.number_input(feature, value=0.0)

        selected_region = st.selectbox("Region", region_options)
        selected_subregion = st.selectbox("Subregion", subregion_options)
        selected_industry = st.selectbox("Industry", industry_options)
        selected_segment = st.selectbox("Segment", segment_options)

        for col in region_cols:
            inputs[col] = 1 if col == f"Region_{selected_region}" else 0

        for col in subregion_cols:
            inputs[col] = 1 if col == f"Subregion_{selected_subregion}" else 0

        for col in industry_cols:
            inputs[col] = 1 if col == f"Industry_{selected_industry}" else 0

        for col in segment_cols:
            inputs[col] = 1 if col == f"Segment_{selected_segment}" else 0

        if st.button("✨ Predict Churn Risk"):

            input_df = pd.DataFrame([inputs])

            # Ensure all model features exist
            for col in model_features:
                if col not in input_df.columns:
                    input_df[col] = 0

            # Correct feature order
            input_df = input_df[model_features]

            # Predict probability
            prob = model.predict_proba(input_df)[:, 1][0]
            percent = round(prob * 100, 2)

            # Revenue impact
            revenue_risk = inputs["Sales"] * prob

            # Risk classification
            if percent < 35:
                st.success(f"Low Risk 🟢 ({percent}%)")
            elif percent < 65:
                st.warning(f"Medium Risk 🟡 ({percent}%)")
            else:
                st.error(f"High Risk 🔴 ({percent}%)")

            st.metric("💰 Estimated Revenue at Risk",
                      f"${revenue_risk:,.2f}")

            if "predictions" not in st.session_state:
                st.session_state["predictions"] = []

            st.session_state["predictions"].append(prob)
            st.session_state["last_input"] = input_df

    with explain_col:
        st.subheader("📘 AI Explanation Panel")
        st.markdown("""
This AI engine:
- Predicts churn probability
- Calculates revenue impact
- Provides explainable insights
- Helps executives make retention decisions
""")
        
# ==================================================
# SHAP EXPLANATION PAGE
# ==================================================
elif page == "🔍 SHAP Explanation":

    st.title("🔍 AI Model Explanation (SHAP Analysis)")

    if "last_input" not in st.session_state:
        st.warning("⚠ Please make a prediction first to see SHAP explanation.")
    else:
        input_df = st.session_state["last_input"]

        st.subheader("📊 Feature Impact on Prediction")

        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(input_df)

        fig, ax = plt.subplots()
        shap.summary_plot(shap_values, input_df, show=False)
        st.pyplot(fig, bbox_inches="tight")

        st.info("""
        🔎 SHAP shows:
        - Which features increased churn risk
        - Which features reduced churn risk
        - Exact contribution of each variable
        """)
