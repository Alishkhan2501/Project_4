import streamlit as st
import time

# Set page config
st.set_page_config(page_title="BMI Calculator", page_icon=":weight_lifter:", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        .main {
            background-color: #f0f8ff;
            padding: 2rem;
            border-radius: 15px;
        }
        .header {
            color: #4CAF50;
            font-size: 2.5rem;
            font-weight: bold;
            text-align: center;
        }
        .subheader {
            color: #333;
            font-size: 1.5rem;
            margin-top: 1rem;
        }
        .result {
            background-color: #e6f7ff;
            padding: 20px;
            border-radius: 10px;
            font-size: 1.25rem;
            font-weight: bold;
            text-align: center;
        }
        .success {
            background-color: #dff0d8;
            color: #3c763d;
            padding: 10px;
            border-radius: 10px;
            font-size: 1.25rem;
            text-align: center;
        }
        .error {
            background-color: #f2dede;
            color: #a94442;
            padding: 10px;
            border-radius: 10px;
            font-size: 1.25rem;
            text-align: center;
        }
        .warning {
            background-color: #fcf8e3;
            color: #8a6d3b;
            padding: 10px;
            border-radius: 10px;
            font-size: 1.25rem;
            text-align: center;
        }
        .slider {
            font-size: 1rem;
            background-color: #e1f5fe;
        }
        .number-input {
            font-size: 1.2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Page header
st.markdown('<div class="header">BMI Calculator by Alix</div>', unsafe_allow_html=True)

# BMI Calculation Instructions
st.markdown("## Enter your weight and height to calculate your BMI")

# Layout with two columns for inputs
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg):", min_value=1.0, format="%.2f")  # Removed the className parameter
with col2:
    height = st.number_input("Height (m):", min_value=0.1, format="%.2f")  # Removed the className parameter

# Check if valid inputs are given
if height > 0 and weight > 0:
    
    # BMI Calculation
    bmi = weight / (height ** 2)
    
    # Show BMI result
    st.markdown(f'<div class="result">Your BMI is: <strong>{bmi:.2f}</strong></div>', unsafe_allow_html=True)
    
    # Show BMI Category
    if bmi < 18.5:
        st.markdown('<div class="error">You are underweight! ⚠️</div>', unsafe_allow_html=True)
    elif 18.5 <= bmi < 24.9:
        st.markdown('<div class="success">You have a normal weight! ✅</div>', unsafe_allow_html=True)
    elif 25 <= bmi < 29.9:
        st.markdown('<div class="warning">You are overweight! ⚠️</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="error">You are obese! ⚠️</div>', unsafe_allow_html=True)
    
    # Show a progress bar indicating BMI range
    if bmi < 18.5:
        progress = 20
    elif 18.5 <= bmi < 24.9:
        progress = 60
    elif 25 <= bmi < 29.9:
        progress = 80
    else:
        progress = 100
    
    # Progress bar for visualization
    st.progress(progress)

    # Animation effect (Optional: You can show a spinning icon)
    with st.spinner('Processing your BMI...'):
        time.sleep(2)
        st.success('Calculation complete!')
    
else:
    st.info("Please enter valid values for weight and height.")