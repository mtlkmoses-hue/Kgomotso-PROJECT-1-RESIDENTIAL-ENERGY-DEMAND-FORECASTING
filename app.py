import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the model
try:
    with open('electricity_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Upload electricity_model.pkl to GitHub.")

st.title("⚡ House Electricity & Appliance Analysis")
sq_ft = st.number_input("Enter Square Footage:", min_value=100, value=1500)

if st.button("Generate Full Report"):
    prediction = model.predict(np.array([[sq_ft]]))[0]
    st.success(f"### Predicted Total: {prediction:.2f} kWh")

    # Appliance Breakdown
    st.subheader("Appliance Breakdown")
    ratios = {"HVAC": 0.45, "Water Heater": 0.18, "Laundry": 0.08, "Lights": 0.07, "Fridge": 0.05}
    data = [{"Appliance": k, "kWh": round(prediction * v, 2)} for k, v in ratios.items()]
    st.table(pd.DataFrame(data))