import streamlit as st
import pickle
import os

# Set up the Streamlit page
st.set_page_config(page_title="Diabetes Prediction", layout="wide", page_icon="🍰")

# Define working directory and load the model
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(f'{working_dir}/diabetes.pkl', 'rb'))

# Initialize BMI and Glucose categories
NewBMI_Underweight = 0
NewBMI_Overweight = 0
NewBMI_Obesity_1 = 0
NewBMI_Obesity_2 = 0 
NewBMI_Obesity_3 = 0
NewInsulinScore_Normal = 0 
NewGlucose_Low = 0
NewGlucose_Normal = 0 
NewGlucose_Overweight = 0
NewGlucose_Secret = 0

# Title for the page
st.title("Diabetes Prediction Using Machine Learning")

# Input fields
col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.text_input("Number of Pregnancies", "0")
with col2:
    Glucose = st.text_input("Glucose Level", "0")
with col3:
    BloodPressure = st.text_input("Blood Pressure Value", "0")
with col1:
    SkinThickness = st.text_input("Skin Thickness Value", "0")
with col2:
    Insulin = st.text_input("Insulin Value", "0")
with col3:
    BMI = st.text_input("BMI Value", "0")
with col1:
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value", "0.0")
with col2:
    Age = st.text_input("Age", "0")

# Predict and display results
diabetes_result = ""
if st.button("Diabetes Test Result"):
    try:
        # Convert inputs to float
        Pregnancies = float(Pregnancies)
        Glucose_val = float(Glucose)
        BloodPressure = float(BloodPressure)
        SkinThickness = float(SkinThickness)
        Insulin_val = float(Insulin)
        BMI_val = float(BMI)
        DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
        Age = float(Age)

        # Set BMI category
        if BMI_val <= 18.5:
            NewBMI_Underweight = 1
        elif 18.5 < BMI_val <= 24.9:
            pass  # Normal BMI
        elif 24.9 < BMI_val <= 29.9:
            NewBMI_Overweight = 1
        elif 29.9 < BMI_val <= 34.9:
            NewBMI_Obesity_1 = 1
        elif 34.9 < BMI_val <= 39.9:
            NewBMI_Obesity_2 = 1
        elif BMI_val > 39.9:
            NewBMI_Obesity_3 = 1

        # Set Insulin score
        if 16 <= Insulin_val <= 166:
            NewInsulinScore_Normal = 1

        # Set Glucose category
        if Glucose_val <= 70:
            NewGlucose_Low = 1
        elif 70 < Glucose_val <= 99:
            NewGlucose_Normal = 1
        elif 99 < Glucose_val <= 126:
            NewGlucose_Overweight = 1
        elif Glucose_val > 126:
            NewGlucose_Secret = 1

        # Prepare user input for prediction
        user_input = [
            Pregnancies, Glucose_val, BloodPressure, SkinThickness, Insulin_val,
            BMI_val, DiabetesPedigreeFunction, Age, NewBMI_Underweight,
            NewBMI_Overweight, NewBMI_Obesity_1, NewBMI_Obesity_2, NewBMI_Obesity_3,
            NewInsulinScore_Normal, NewGlucose_Low, NewGlucose_Normal,
            NewGlucose_Overweight, NewGlucose_Secret
        ]

        # Make prediction
        prediction = diabetes_model.predict([user_input])
        if prediction[0] == 1:
            diabetes_result = "The person has diabetes."
        else:
            diabetes_result = "The person does not have diabetes."
    except ValueError:
        diabetes_result = "Please enter valid numerical values for all inputs."

st.success(diabetes_result)
