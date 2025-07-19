import streamlit as st
import pandas as pd
import joblib

model = joblib.load("loan_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.set_page_config(page_title="Loan Approval Predictor", page_icon="🏦")

st.title("🏦 Loan Approval Prediction App")
st.write("Fill in the details to check if your loan would be approved.")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_term = st.selectbox("Loan Term (in months)", [12, 36, 60, 84, 120, 180, 240, 300, 360, 480])
credit_history = st.selectbox("Credit History", ["Good (1)", "Bad (0)"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])


## Mapping input to encoded values
def encode_input():
    return pd.DataFrame([[
        0 if gender == "Female" else 1,
        1 if married == "Yes" else 0,
        {"0": 0, "1": 1, "2": 2, "3+": 3}[dependents],
        0 if education == "Graduate" else 1,
        1 if self_employed == "Yes" else 0,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        1.0 if credit_history == "Good (1)" else 0.0,
        {"Urban": 2, "Semiurban": 1, "Rural": 0}[property_area]
    ]], columns=[
        "Gender", "Married", "Dependents", "Education", "Self_Employed",
        "ApplicantIncome", "CoapplicantIncome", "LoanAmount",
        "Loan_Amount_Term", "Credit_History", "Property_Area"
    ])

input_df = encode_input()

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    result = "✅ Approved" if prediction == 1 else "❌ Rejected"
    st.subheader("Prediction Result:")
    st.write(result)
