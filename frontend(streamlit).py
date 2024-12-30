import streamlit as st
import pandas as pd
import numpy as np
import pickle

model_filename = 'trained_model.pkl'
try:
    with open(model_filename, 'rb') as f:
        model_data = pickle.load(f)
    weights = model_data['weights']
    preprocessor = model_data['preprocessor']
except FileNotFoundError:
    st.error("The model file was not found. Please check the file path.")
    st.stop()

st.title("Space Traffic Density Prediction")

st.header("Input Parameters")
location = st.selectbox("Select Location:", ["Orbit LEO", "Orbit GEO", "Orbit MEO", "Other"])
object_type = st.selectbox("Select Object Type:", ["Satellite", "Debris", "Spacecraft", "Other"])
peak_time = st.text_input("Enter Peak Time (e.g., 15:00):", value="15:00")

if st.button("Predict Traffic Density"):
    try:
        input_data = pd.DataFrame({
            'Location': [location],
            'Object_Type': [object_type],
            'Peak_Time': [peak_time]
        })

        transformed_input = preprocessor.transform(input_data).toarray()
        transformed_input = np.c_[np.ones((transformed_input.shape[0], 1)), transformed_input]
        prediction = np.dot(transformed_input, weights).flatten()

        st.success(f"Predicted Traffic Density: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
