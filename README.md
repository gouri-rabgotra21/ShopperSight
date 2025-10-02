# ShopperSight: A Fashion E-commerce Analytics Platform

This project analyzes a large e-commerce dataset to predict customer purchase behavior and segment customers into distinct groups using machine learning. The project is presented as an interactive web dashboard built with Streamlit.

## Features
- **Purchase Prediction:** A Random Forest model predicts the likelihood of a purchase event.
- **Customer Segmentation:** K-Means clustering is used to group customers into 4 behavioral segments.
- **Interactive Dashboard:** A Streamlit application allows for live predictions and exploration of the customer segments.

## How to Run
1. Install the required libraries: `pip install -r requirements.txt`
2. Run the Jupyter Notebook to train the models and generate the assets: `1_Data_Analysis_and_Modeling.ipynb`
3. Launch the Streamlit web app: `streamlit run app.py`