import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="SmartCart Customer Segmentation",
    page_icon="🛒",
    layout="wide"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #eef2f3, #d9e4f5);
}

.main {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 14px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.08);
}

h1, h2, h3 {
    color: #1f2c3a;
}

.metric-box {
    background: #f7fafc;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.06);
}

.result-card {
    margin-top: 20px;
    padding: 20px;
    border-radius: 12px;
    background: #f0fff4;
    border-left: 6px solid #38a169;
    font-size: 18px;
    font-weight: 600;
    color: #2d3748;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Load Model ----------------
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

FEATURES = scaler.feature_names_in_

# ---------------- Title ----------------
st.title("🛒 SmartCart Customer Segmentation System")
st.write(
    "This application uses machine learning to group customers into meaningful segments, "
    "helping business teams identify high-value and low-engagement customers easily."
)

st.divider()

# ================= LEFT: INPUT | RIGHT: INFO =================
left, right = st.columns([1.1, 1])

# ---------------- LEFT: INPUT FORM ----------------
with left:
    st.subheader("📊 Customer Information")

    income = st.number_input("Income", 0)
    age = st.number_input("Age", 18)
    recency = st.number_input("Recency (days)", 0)
    tenure = st.number_input("Customer Tenure (days)", 0)
    total_spending = st.number_input("Total Spending", 0)
    total_children = st.number_input("Total Children", 0)

    st.subheader("🛍️ Purchase Behaviour")
    deals = st.number_input("Deals Purchases", 0)
    web_p = st.number_input("Web Purchases", 0)
    catalog_p = st.number_input("Catalog Purchases", 0)
    store_p = st.number_input("Store Purchases", 0)
    web_visits = st.number_input("Web Visits / Month", 0)

    st.subheader("🎓 Education")
    edu = st.radio("Education Level", ["Graduate", "Postgraduate", "Undergraduate"])

    edu_grad = 1 if edu == "Graduate" else 0
    edu_post = 1 if edu == "Postgraduate" else 0
    edu_under = 1 if edu == "Undergraduate" else 0

    st.subheader("🏠 Living Status")
    living = st.radio("Living With", ["Partner", "Alone"])
    living_partner = 1 if living == "Partner" else 0
    living_alone = 1 if living == "Alone" else 0

    complain = st.selectbox("Complain", [0, 1])
    response = st.selectbox("Response", [0, 1])

# ---------------- RIGHT: BUSINESS INFO ----------------
with right:
    st.subheader("📌 Cluster Meaning (Business View)")

    st.markdown("""
    - **Cluster 0** → Low Value, Price-Sensitive Customers  
    - **Cluster 1** → High Value & Loyal Customers  
    - **Cluster 2** → Low Engagement Customers  
    - **Cluster 3** → Premium & High Spending Customers  
    """)

    st.subheader("📈 Why this matters?")
    st.markdown("""
    - Helps marketing teams personalize offers  
    - Identifies churn-risk customers early  
    - Improves customer retention strategies  
    """)

# ---------------- Prediction ----------------
st.divider()

if st.button("🔍 Predict Customer Segment"):

    input_df = pd.DataFrame([[
        income, recency, deals, web_p, catalog_p, store_p,
        web_visits, complain, response, age, tenure,
        total_spending, total_children,
        edu_grad, edu_post, edu_under,
        living_alone, living_partner
    ]], columns=FEATURES)

    scaled = scaler.transform(input_df)
    cluster = model.predict(scaled)[0]

    cluster_map = {
        0: "Low Value – Price Sensitive",
        1: "High Value – Loyal Customers",
        2: "Low Engagement Customers",
        3: "Premium & High Spending Customers"
    }

    st.markdown(
        f"""
        <div class="result-card">
            ✅ Predicted Cluster: <b>{cluster}</b><br>
            {cluster_map.get(cluster)}
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- VISUAL EVALUATION ----------------
st.subheader("📊 Visual Insights (Easy to Understand)")

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# ---------- Donut Chart: Financial Distribution ----------
finance_labels = ["Income", "Total Spending"]
finance_values = [income, total_spending]

if sum(finance_values) > 0:
    ax[0].pie(
        finance_values,
        labels=finance_labels,
        autopct="%1.1f%%",
        startangle=90,
        wedgeprops=dict(width=0.4)
    )
    ax[0].set_title("Customer Financial Distribution")
else:
    ax[0].text(
        0.5, 0.5,
        "Enter income or spending\n to view chart",
        ha="center", va="center", fontsize=12
    )
    ax[0].set_title("Customer Financial Distribution")

# ---------- Pie Chart: Engagement Breakdown ----------
engagement_labels = ["Web Purchases", "Store Purchases", "Web Visits"]
engagement_values = [web_p, store_p, web_visits]

if sum(engagement_values) > 0:
    ax[1].pie(
        engagement_values,
        labels=engagement_labels,
        autopct="%1.1f%%",
        startangle=90
    )
    ax[1].set_title("Customer Engagement Breakdown")
else:
    ax[1].text(
        0.5, 0.5,
        "Enter engagement data\n to view chart",
        ha="center", va="center", fontsize=12
    )
    ax[1].set_title("Customer Engagement Breakdown")

st.pyplot(fig)
