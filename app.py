import streamlit as st
import pickle
# Load the trained model
rf_model = pickle.load(open("rf_model.pkl", "rb"))
# Title
st.title("Employee Prediction")
st.subheader("Personal Details")
st.text("Machine Learning Deployment")
st.write("Welcome to my application")
# User Inputs
name = st.text_input("Enter your name")
gender1 = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

gender = 1 if gender1 == "Male" else 0
age = st.number_input("Age", min_value=18, max_value=65)
DistanceFromHome_KM = st.number_input(
    "Distance From Home (KM)",
    min_value=0
)

Salary = st.number_input(
    "Salary",
    min_value=0
)

# Prediction
if st.button("Predict"):

    prediction = rf_model.predict(
        [[gender, age, DistanceFromHome_KM, Salary]]
    )

    st.success(f"Prediction completed for {name}")

    if prediction[0] == 1:
        st.error("Employee is likely to leave.")
    else:
        st.success("Employee is likely to stay.")
