from fastapi import FastAPI
import joblib
import numpy as np
from schema import Transaction

app = FastAPI(title="SecureBank Fraud Detection API")

# Load model ONCE at startup
model = joblib.load(
    r"C:\Users\Prasad\Desktop\secure-bank-fraud-ml\models\fraud_lgbm_final.pkl"
)

@app.get("/")
def home():
    return {"message": "SecureBank Fraud Detection API is running"}

@app.post("/predict")
def predict_fraud(txn: Transaction):
    
    data = np.array([[
        txn.amount,
        txn.oldbalanceOrg,
        txn.newbalanceOrig,
        txn.oldbalanceDest,
        txn.newbalanceDest,
        txn.isFlaggedFraud,
        txn.hour_of_day,
        txn.day,
        txn.log1p_amount,
        txn.amount_to_balance_ratio,
        txn.is_high_amount,
        txn.balance_diff_org,
        txn.balance_error,
        txn.type_CASH_OUT,
        txn.type_DEBIT,
        txn.type_PAYMENT,
        txn.type_TRANSFER
    ]])

    prob = model.predict_proba(data)[0][1]
    prediction = int(prob >= 0.2)

    risk = (
        "HIGH" if prob >= 0.7 else
        "MEDIUM" if prob >= 0.3 else
        "LOW"
    )

    return {
        "fraud_probability": round(float(prob), 4),
        "fraud_prediction": prediction,
        "risk_level": risk
    }
