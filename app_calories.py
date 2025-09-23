import streamlit as st
import numpy as np
import joblib


model = joblib.load("model.pkl")
scaler_X = joblib.load("scaler_X.pkl")
scaler_y = joblib.load("scaler_y.pkl")


# Page config
st.set_page_config(
    page_title="Calories Predictor",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Calories Prediction App")
st.markdown(
    "Enter your personal information and daily activity to predict the number of calories burned."
)


# User Input
st.subheader("Personal Info")
age = st.number_input("Age (years)", min_value=10, max_value=100, value=25)
gender = st.selectbox("Gender", options=["Male", "Female"])

st.subheader("Body Info")
height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=65)

st.subheader("Activity")
duration = st.slider("Exercise Duration (minutes)", min_value=0, max_value=300, value=30, step=5)

st.subheader("Optional Info")
heart_rate = st.number_input("Average Heart Rate (bpm)", min_value=0, max_value=200, value=70)
body_temp = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=50.0, value=36.5, step=0.1)


# Encode gender with correct logic
gender_encoding = {"Female": 0, "Male": 1}
gender_encoded = gender_encoding.get(gender)


# Prepare input array and handle NaN
user_input = np.array([[age, gender_encoded, height, weight, duration, heart_rate, body_temp]])
user_input_scaled = scaler_X.transform(user_input)


# Prediction
if st.button("🔥 Predict Calories"):
    try:
        pred_scaled = model.predict(user_input_scaled)
        pred_calories = scaler_y.inverse_transform(pred_scaled.reshape(-1,1))[0][0]

        # Determine category
        if pred_calories < 150:
            category = "Low 🔹"
            tips = """
            - Increase light physical activity like walking or stretching.
            - Monitor your food intake carefully.
            - Stay hydrated.
            - Include more protein in your diet.
            """
        elif pred_calories <= 400:
            category = "Ideal 🟢"
            tips = """
            - Your activity level is sufficient.
            - Maintain a balanced diet.
            - Keep a regular sleep schedule.
            - Include strength training exercises.
            - Monitor daily exercise duration to stay active.
            """
        else:
            category = "High 🔥"
            tips = """
            - High calorie burn, suitable for intense activity.
            - Ensure proper nutrition and hydration.
            - Include rest and recovery periods.
            - Monitor heart rate during exercises.
            - Combine cardio and resistance training for better results.
            """
        
        # Display results
        st.success(f"Predicted Daily Calories Burned: **{pred_calories:.2f} kcal**")
        st.info(f"Category: **{category}**")
        st.markdown("**Tips:**")
        st.markdown(tips)
    except Exception as e:
        st.error(f"An error occurred: {e}")