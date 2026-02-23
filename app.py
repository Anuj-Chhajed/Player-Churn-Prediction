import streamlit as st
import pandas as pd
import joblib

model = joblib.load("churn_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("Player Churn Prediction System")

uploaded_file = st.file_uploader("Upload Player Data CSV", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    data = data.drop("PlayerID", axis=1)

    data["churn"] = (data["EngagementLevel"] == "Low").astype(int)

    data = data.drop("EngagementLevel", axis=1)

    data = pd.get_dummies(data, drop_first=True)

    for col in model_columns:
        if col not in data.columns:
            data[col] = 0

    data = data[model_columns]

    predictions = model.predict(data)
    probabilities = model.predict_proba(data)[:, 1]

    result = pd.DataFrame({
        "Churn Prediction (0=No, 1=Yes)": predictions,
        "Churn Probability": probabilities
    })

    st.subheader("Prediction Results")
    st.write(result)