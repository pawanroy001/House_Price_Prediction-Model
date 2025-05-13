import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("house_model_new.pkl")

st.title("🏠 House Price Prediction App")

# House Style Encoding
style_mapping = {
    "1 Story": 0,
    "2 Story": 1,
    "Split Level": 2,
    "Duplex": 3
}

# Collect user input
area = st.number_input("Lot Area (sq ft)", 1000, 100000, step=100)
year_built = st.number_input("Year Built", 1900, 2026)
bedrooms = st.number_input("Number of Bedrooms", 1, 10, step=1)
house_style = st.selectbox("House Style", list(style_mapping.keys()))
overall_qual = st.slider("Overall Quality (1–10)", 1, 10)


usd_to_inr = 84

# Prepare data for prediction
if st.button("Predict Price"):
    style_value = style_mapping[house_style]  # Convert to numeric
    input_data = np.array([[float(area), float(year_built), float(overall_qual), float(bedrooms), float(style_value)]])
    prediction = model.predict(input_data)[0]
    prediction_inr = prediction * usd_to_inr

   
    st.success(f"🏡 Predicted House Price:₹{int(prediction_inr):,}")

       

    