# 🛒 SmartCart Customer Segmentation System

An end-to-end **Machine Learning powered customer segmentation system** built to help businesses understand customer behavior and make smarter marketing decisions.

🚀 **Live Demo:**  
👉 https://smartcart-customer-segmentation.streamlit.app  
*(Replace with your actual Streamlit Cloud link)*

---

## 🎯 Project Objective

Most e-commerce platforms use **one generic strategy for all customers**, which leads to:
- ❌ Inefficient marketing
- ❌ Missed high-value customers
- ❌ Poor customer retention

This project solves that by using **unsupervised machine learning** to group customers into meaningful segments based on spending, engagement, and demographics.

---

## 📊 Dataset Overview

- 👥 **Customers:** 2,240  
- 📦 **Features:** 22 (Demographics, Purchase Behavior, Engagement)
- 🧹 Cleaned & engineered into **18 final training features**

Key attributes:
- Income, Age, Recency
- Web / Store / Catalog purchases
- Total spending & family size
- Education level & living status

---

## 🧠 Feature Engineering Highlights

✨ Real-world feature engineering was applied:

- 🎂 **Age** derived from birth year  
- ⏳ **Customer_Tenure_Days** from enrollment date  
- 💰 **Total_Spending** aggregated across product categories  
- 👨‍👩‍👧 **Total_Children** from household data  
- 🏷️ One-hot encoding for categorical features (Education, Living Status)

---

## 🤖 Machine Learning Approach

- 🔹 Feature Scaling using **StandardScaler**
- 🔹 Unsupervised learning with **KMeans Clustering**
- 🔹 Optimal clusters selected using:
  - 📉 Elbow Method
  - 📊 Silhouette Score
- 🔹 Final model trained with **4 customer clusters**

---

## 📌 Customer Segments Identified

| Cluster | Description |
|-------|------------|
| 🟢 Cluster 0 | Low Value & Price-Sensitive Customers |
| 🔵 Cluster 1 | High Value & Loyal Customers |
| 🟠 Cluster 2 | Low Engagement Customers |
| 🟣 Cluster 3 | Premium & High Spending Customers |

---

## 🖥️ Web Application (Streamlit)

A modern and interactive **Streamlit dashboard** was built to:

- 🧾 Take customer details as input  
- 🔍 Predict customer segment in real time  
- 🍩 Show **donut & pie charts** for easy understanding  
- 💼 Explain results in **business-friendly language**

⚠️ Edge cases (like zero input values) are safely handled to avoid UI crashes.

---

## 🛠️ Tech Stack

- 🐍 Python  
- 📊 Pandas, NumPy  
- 🤖 Scikit-learn  
- 📈 Matplotlib, Seaborn  
- 🌐 Streamlit  

---

## 🚀 Real-World Use Cases

- 🎯 Personalized marketing campaigns  
- 🔁 Customer retention planning  
- ⚠️ Early churn-risk identification  
- 📈 Business decision support  

---

## 📚 Key Learnings

- End-to-end ML pipeline design
- Feature consistency between training & deployment
- Handling real-world deployment edge cases
- Translating ML results into actionable business insights

---

## 🙌 Author

**Ankit Gupta**  
📧 Email: ankig4515@gmail.com  
💼 Aspiring AI/ML Engineer | Data Science Enthusiast
