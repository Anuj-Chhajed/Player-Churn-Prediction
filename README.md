# Intelligent Player Churn Prediction System (Milestone 1)

##  Project Overview
Player churn refers to the situation where players stop engaging with a game over time. Predicting player churn is important for gaming companies as it helps in improving player retention, engagement strategies, and overall user experience.

This project implements a **machine learning–based churn prediction system** using historical gameplay and engagement data. A supervised learning model is trained to identify players who are likely to churn, and predictions are displayed through a simple web-based user interface.

This repository contains the **Milestone-1 implementation**, which focuses strictly on traditional machine learning methods (no GenAI or agentic AI).

---

##  Objective
- Predict player churn using historical gameplay and engagement data  
- Apply data preprocessing and feature engineering  
- Train and evaluate a supervised ML model  
- Provide a basic user interface to display churn predictions  

---

##  Dataset
- **Source:** Kaggle – Online Gaming Behavior Dataset  
- **Type:** CSV file containing player demographics, gameplay statistics, and engagement metrics  

### Key Features Used
- Sessions per week  
- Average session duration  
- Total playtime  
- Player level and achievements  
- In-game purchases  
- Engagement level  

### Target Variable
The dataset does not explicitly contain a churn label.  
Churn is derived as follows:

- **Low Engagement → Churn (1)**
- **Medium / High Engagement → Not Churn (0)**

---

##  Machine Learning Approach
- **Type:** Supervised Learning (Binary Classification)
- **Model Used:** Logistic Regression
- **Library:** scikit-learn

### Preprocessing Steps
- Removal of non-informative columns (`PlayerID`)
- Handling missing values
- One-hot encoding of categorical features
- Train-test split (80:20)

---

##  Model Evaluation
The model is evaluated using standard classification metrics:
- Accuracy
- Precision
- Recall
- F1-score

**Achieved Accuracy:** ~87.7%

This performance indicates that the model effectively learns player behavior patterns related to churn.

---

##  User Interface
A lightweight web interface is built using **Streamlit**.

### Features:
- Upload player data in CSV format
- Predict churn for one or multiple players
- Display churn prediction and churn probability