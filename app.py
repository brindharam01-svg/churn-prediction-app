import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model and columns
model = pickle.load(open("churn_model.pkl", "rb"))
columns = pickle.load(open("model_columns.pkl", "rb"))

st.title("Bank Customer Churn Prediction")

# =========================
# USER INPUTS
# =========================

credit_score = st.number_input("Credit Score", 300, 900)
age = st.number_input("Age", 18, 100)
tenure = st.number_input("Tenure (years)", 0, 10)
balance = st.number_input("Balance")
num_products = st.number_input("Number of Products", 1, 4)
has_card = st.selectbox("Has Credit Card", [0, 1])
is_active = st.selectbox("Is Active Member", [0, 1])
salary = st.number_input("Estimated Salary")

gender = st.selectbox("Gender", ["Male", "Female"])
geo = st.selectbox("Geography", ["France", "Germany", "Spain"])

# =========================
# CREATE INPUT DATAFRAME
# =========================

input_df = pd.DataFrame(columns=columns)
input_df.loc[0] = 0  # initialize all values as 0

# Fill numeric values
input_df['CreditScore'] = credit_score
input_df['Age'] = age
input_df['Tenure'] = tenure
input_df['Balance'] = balance
input_df['NumOfProducts'] = num_products
input_df['HasCrCard'] = has_card
input_df['IsActiveMember'] = is_active
input_df['EstimatedSalary'] = salary

# Gender
if 'Gender_Male' in input_df.columns:
    input_df['Gender_Male'] = 1 if gender == "Male" else 0

# Geography
if 'Geography_Germany' in input_df.columns:
    input_df['Geography_Germany'] = 1 if geo == "Germany" else 0

if 'Geography_Spain' in input_df.columns:
    input_df['Geography_Spain'] = 1 if geo == "Spain" else 0

# =========================
# PREDICTION
# =========================

if st.button("Predict"):
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("Customer is likely to churn ❌")
    else:
        st.success("Customer will stay ✅")