# app.py

import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the pre-trained pipeline
with open("final_pipeline.pkl", "rb") as file:
    model_pipeline = pickle.load(file)

# Streamlit app
st.title("Car Price Prediction App")
st.write("Enter the car details to predict its price.")

# Input fields for user data
condition = st.selectbox(
    "Condition", 
    ["salvage", "fair", "unknown", "good", "excellent", "like new", "new"]
)
model = st.text_input("Model (e.g., Corolla, Civic)")
manufacturer = st.text_input("Manufacturer (e.g., Toyota, Honda)")
fuel = st.selectbox("Fuel Type", ["gas", "diesel", "electric", "hybrid", "other"])
cylinders = st.selectbox("Cylinders", ["3 cylinders", "4 cylinders", "5 cylinders", 
                                       "6 cylinders", "8 cylinders", "10 cylinders", 
                                       "12 cylinders", "other"])
title_status = st.selectbox(
    "Title Status", 
    ["clean", "salvage", "rebuilt", "lien", "parts only", "missing"]
)
transmission = st.selectbox("Transmission", ["manual", "automatic", "other"])
drive = st.selectbox("Drive Type", ["4wd", "fwd", "rwd", "other"])
car_type = st.text_input("Type (e.g., sedan, suv, truck)")
paint_color = st.text_input("Paint Color (e.g., white, black, red)")
odometer = st.number_input("Odometer Reading (miles)", min_value=0, value=50000)

# Collect inputs into a DataFrame
input_data = pd.DataFrame({
    "condition": [condition],
    "model": [model],
    "manufacturer": [manufacturer],
    "fuel": [fuel],
    "cylinders": [cylinders],
    "title_status": [title_status],
    "transmission": [transmission],
    "drive": [drive],
    "type": [car_type],
    "paint_color": [paint_color],
    "odometer": [odometer]
})

# Make prediction when the user submits data
if st.button("Predict Price"):
    prediction = model_pipeline.predict(input_data)
    st.success(f"Estimated Car Price: ${prediction[0]:,.2f}")