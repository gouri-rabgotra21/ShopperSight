# app.py
import streamlit as st
import pandas as pd
import joblib
import os

# --- CONFIGURATION ---
st.set_page_config(page_title="ShopperSight Analytics", layout="wide")

# --- LOAD SAVED ASSETS ---
# Use @st.cache_data for older Streamlit versions, @st.cache_resource for newer ones for models
@st.cache_resource
def load_models():
    purchase_model = joblib.load(os.path.join('saved_models', 'purchase_model.pkl'))
    return purchase_model

@st.cache_data
def load_data():
    customer_segments_df = pd.read_csv('customer_segments.csv')
    return customer_segments_df

purchase_model = load_models()
customer_segments_df = load_data()


# --- APP LAYOUT ---
st.title("🛍️ ShopperSight: E-Commerce Analytics Dashboard")
st.write("""
This interactive dashboard provides insights from a large fashion e-commerce dataset.
It includes a **Purchase Prediction Model** and **Customer Segmentation Analysis**.
""")

# --- Display Customer Segments ---
st.header("👥 Customer Segmentation")
st.write("Customers who have made at least one purchase have been segmented into 4 groups based on their behavior.")
st.dataframe(customer_segments_df)

# --- Interactive Prediction ---
st.header("🔮 Live Purchase Prediction")
st.write("Select features to see a real-time prediction from our Random Forest model.")

visitor_id = st.number_input("Enter a Visitor ID", min_value=0, value=12345, step=1)
item_id = st.number_input("Enter an Item ID", min_value=0, value=54321, step=1)

if st.button("Predict Purchase"):
    features = pd.DataFrame({'visitorid': [visitor_id], 'itemid': [item_id]})
    prediction = purchase_model.predict(features)
    prediction_proba = purchase_model.predict_proba(features)
    
    if prediction[0] == 1:
        st.success(f"Prediction: **Likely to Purchase** (Confidence: {prediction_proba[0][1]*100:.2f}%)")
    else:
        st.error(f"Prediction: **Unlikely to Purchase** (Confidence: {prediction_proba[0][0]*100:.2f}%)")