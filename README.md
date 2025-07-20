#🏦 Loan Approval Prediction App

This is a Machine Learning project that predicts whether a loan application will be approved based on applicant details such as income, credit history, education, employment status, and more.

The project includes:
- A trained Random Forest classifier using the Loan Prediction Dataset from Kaggle
- A user-friendly frontend built using Streamlit
- Deployment to Streamlit Cloud for interactive web access

---

 📌 Features

- ✅ User input form for all loan application fields
- 🤖 Predicts loan approval (Approved / Rejected)
- 📊 Clean UI powered by Streamlit
- 💾 Model loaded using `joblib`
- ⚙️ Fully deployed and accessible online

---

# 🚀 Live Demo

👉 [Click here to try the app](https://loanapprovalapp-lntbkuskztcbrul2pzxrju.streamlit.app/)

> Replace the link with your actual Streamlit Cloud app URL

---

## 🧠 How It Works

1. Model trained using a RandomForestClassifier on preprocessed data
2. Model and column order saved using `joblib`
3. Streamlit app:
   - Takes user input
   - Encodes it to match training format
   - Loads the model and predicts
   - Displays the result (Approved / Rejected)

---

## 📁 Files in This Repository

| File | Description |
|------|-------------|
| `app.py` | Streamlit web app frontend |
| `loan_model.pkl` | Trained ML model |
| `model_columns.pkl` | List of feature columns used for training |
| `requirements.txt` | Dependencies for the app |
| `README.md` | Project description |
