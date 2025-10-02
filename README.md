# ShopperSight

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-brightgreen.svg)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange.svg)](https://scikit-learn.org/stable/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

ShopperSight is a fashion e-commerce analytics platform that predicts customer purchase behavior and segments users into meaningful clusters. The project includes a machine learning pipeline and an interactive web dashboard (built with Streamlit) for visualization and prediction.

---

## Features

- Purchase Prediction — Uses a Random Forest model to estimate the probability that a user will make a purchase  
- Customer Segmentation — Applies K-Means clustering to categorize users into 4 behavioral groups  
- Interactive Dashboard — Streamlit app to explore customer segments and run live predictions  
- Data Analysis Notebook — A Jupyter Notebook covering exploratory data analysis, feature engineering, and model building  

---

## Repository Structure
.
├── README.md
├── app.py
├── requirements.txt
├── 1_Data_Analysis_and_Modeling.ipynb
├── customer_segments.csv
└── saved_models/


- `app.py` — Main Streamlit application  
- `requirements.txt` — Python package dependencies  
- `1_Data_Analysis_and_Modeling.ipynb` — Notebook for data exploration, model training, etc.  
- `customer_segments.csv` — Data used for segment visualization  
- `saved_models/` — Folder containing serialized or trained model files  

---

## Installation & Setup

1. Clone the repository  
   ```bash
   git clone https://github.com/gouri-rabgotra21/ShopperSight.git
   cd ShopperSight
   
2.Install dependencies

pip install -r requirements.txt

3.Train the models (if not already provided)

Open 1_Data_Analysis_and_Modeling.ipynb

Run through the notebook to generate model artifacts and data needed for dashboard

4.Run the web app

streamlit run app.py

5.Access the dashboard in your browser (usually at http://localhost:8501)

How It Works (High Level)

Data Processing & Training

Clean and preprocess raw e-commerce data

Feature engineering to derive relevant metrics

Train a Random Forest classifier for purchase prediction

Use K-Means clustering to derive four customer segments

Web Dashboard

Users can input features for a hypothetical user and get purchase probability

Visualize segment-wise statistics and insights

Explore cluster characteristics

Requirements

See requirements.txt for full dependencies. Some typical packages include:

pandas, numpy

scikit-learn

streamlit

matplotlib, seaborn

Notes & Tips

Ensure the saved_models/ directory has the serialized models (e.g. .pkl files) used by app.py. If not, run the notebook to generate them.

Match the input features in the Streamlit app to the features used in training (same preprocessing steps).

The clustering assumes 4 segments — this is a design choice and may be tuned.

License & Attribution

You may add a license (e.g. MIT, Apache 2.0) if you intend for open use.
If you build upon external datasets or code, provide proper attribution.


Do you also want me to generate a **LICENSE file (MIT template)** so the badge works correctly?

Gouri Rabgotra 
