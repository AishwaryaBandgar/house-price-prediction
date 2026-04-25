# streamlit run app.py
import streamlit as st
import numpy as np
import joblib

# -------------------------------
# Load Model
# -------------------------------
model = joblib.load("outputs/model.pkl")

# -------------------------------
# App Title
# -------------------------------
st.title("🏠 House Price Prediction App")

st.write(
    "Predict house prices based on area, bedrooms, house age, and distance from city center."
)

# -------------------------------
# User Inputs
# -------------------------------
st.sidebar.header("Enter House Details")

area = st.sidebar.slider("Area (sq ft)", 500, 3000, 1500)
bedrooms = st.sidebar.slider("Bedrooms", 1, 5, 3)
house_age = st.sidebar.slider("House Age (years)", 0, 30, 10)
distance = st.sidebar.slider("Distance from City Center (km)", 1, 20, 5)

# -------------------------------
# Prediction
# -------------------------------
input_data = np.array([[area, bedrooms, house_age, distance]])

prediction = model.predict(input_data)[0]

# -------------------------------
# Output
# -------------------------------
st.subheader("Predicted Price")

st.success(f"Estimated House Price: {prediction:.2f}")

# -------------------------------
# Info Section
# -------------------------------
st.markdown("---")
st.markdown("### 📌 Model Info")
st.write("Model: Linear Regression")
st.write("Features used: Area, Bedrooms, House Age, Distance")

st.markdown("### ⚠️ Disclaimer")
st.write("This model is trained on synthetic data and is for demonstration purposes only.")