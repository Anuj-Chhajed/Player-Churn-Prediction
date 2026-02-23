import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("data/online_gaming_behavior_dataset.csv")

df = df.drop("PlayerID", axis=1)

df["churn"] = (df["EngagementLevel"] == "Low").astype(int)

df = df.drop("EngagementLevel", axis=1)

df = df.dropna()

df = pd.get_dummies(df, drop_first=True)

X = df.drop("churn", axis=1)
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

joblib.dump(model, "churn_model.pkl")
joblib.dump(X.columns.tolist(), "model_columns.pkl")

print("Model training completed and saved.")