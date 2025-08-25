import streamlit as st
import numpy as np
import pickle

# Load the best model
with open("best_model.pkl", "rb") as file:
    best_model = pickle.load(file)

# Streamlit interface
st.title("Rainfall Prediction System 🌧️")
st.write("Enter the weather conditions below to predict the expected precipitation:")

# User-friendly feature names with correct 14 inputs
high_temp = st.number_input("Highest Temperature of the Day (°F)")
avg_temp = st.number_input("Average Temperature of the Day (°F)")
low_temp = st.number_input("Lowest Temperature of the Day (°F)" )

high_dewpoint = st.number_input("Highest Dew Point (°F)")
avg_dewpoint = st.number_input("Average Dew Point (°F)")
low_dewpoint = st.number_input("Lowest Dew Point (°F)")

high_humidity = st.number_input("Maximum Humidity (%)")
avg_humidity = st.number_input("Average Humidity (%)")
low_humidity = st.number_input("Minimum Humidity (%)")

avg_pressure = st.number_input("Average Atmospheric Pressure (inches)")

high_visibility = st.number_input("Maximum Visibility (miles)")
avg_visibility = st.number_input("Average Visibility (miles)")
low_visibility = st.number_input("Minimum Visibility (miles)")

avg_wind = st.number_input("Average Wind Speed (MPH)")

if st.button("Predict Precipitation"):
    # Creating input array with exactly 14 features
    user_input = np.array([[high_temp, avg_temp, low_temp, high_dewpoint, avg_dewpoint, low_dewpoint, 
                            high_humidity, avg_humidity, low_humidity, avg_pressure, 
                            high_visibility, avg_visibility, low_visibility, avg_wind]])

    prediction = best_model.predict(user_input)
    st.write(f"🌧️ Predicted Rainfall: {prediction[0]:.2f} inches")
