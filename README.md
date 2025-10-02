# ShopperSight: E-commerce Customer Analytics Platform

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Table of Contents
1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Dashboard Preview](#dashboard-preview)
4. [Project Workflow](#project-workflow)
5. [Analysis & Results](#analysis--results)
6. [Tech Stack](#tech-stack)
7. [Setup and Local Installation](#setup-and-local-installation)
8. [License](#license)

---

## Overview

ShopperSight is an end-to-end data science project that analyzes a large-scale e-commerce dataset (over 2.7 million events) to derive actionable business insights. The project features:

- A **supervised machine learning model** to predict customer purchase intent  
- An **unsupervised clustering model** to segment shoppers into distinct behavioral groups  

The entire pipeline, from data processing to prediction, is showcased through a user-friendly, interactive **web dashboard built with Streamlit**.  

This project demonstrates a typical data science workflow including data cleaning, feature engineering, model training, evaluation, and deployment.

---

## Key Features

- **Purchase Likelihood Prediction:** Predicts the probability of a user event leading to a transaction using a Random Forest Classifier.  
- **Customer Segmentation:** Uses K-Means clustering to identify distinct customer personas for targeted business strategies.  
- **Interactive Web Dashboard:** Streamlit app provides live predictions and interactive exploration of customer segments.  

---

## Dashboard Preview

*A preview of the live, interactive dashboard built with Streamlit.*

![ShopperSight Dashboard](image_53d62e.jpg)  
*Note: Ensure this image is pushed to your GitHub repository.*

---

## Project Workflow

The project follows a standard data science pipeline, from raw data to a deployed data application.

```mermaid
graph TD;
    A[1. Raw Data (.csv)] --> B{2. Jupyter Notebook};
    B --> |Data Cleaning, EDA, Training| C[3. Trained Models (.pkl)];
    B --> |Aggregation| D[4. Segmented Data (.csv)];
    C --> E{5. Streamlit App};
    D --> E;
    E --> F[6. Interactive Dashboard];
Analysis & Results
1. Purchase Prediction Model Performance

The Random Forest model was evaluated on a held-out test set. The confusion matrix below visualizes performance distinguishing "Purchased" vs. "Not Purchased" events.

Ensure the corresponding .png is generated from your notebook and pushed to GitHub.

2. Customer Segment Analysis
Cluster ID	Persona	Characteristics
0	High-Value Champions	High views, add-to-carts, and transactions. Most engaged and valuable users.
1	Potential Loyalists	Moderate activity. Consistent, with potential to grow into Champions.
2	Window Shoppers	Very high views, very low transactions. Browse a lot but rarely buy.
3	New / Infrequent Buyers	Low activity in all metrics. Likely new or rare customers.

Ensure the segment analysis images are saved and included in the repo.

Tech Stack
Category	Technologies
Programming Language	Python
Core Libraries	Pandas, NumPy, Scikit-learn, Joblib
Web Framework	Streamlit
Data Visualization	Matplotlib, Seaborn
Development Tools	VS Code, Jupyter Notebooks, Git, GitHub
Setup and Local Installation

Follow these steps to run the project locally:

Clone the Repository

git clone https://github.com/gouri-rabgotra21/ShopperSight.git
cd ShopperSight


Install Dependencies
(Recommended: use a virtual environment)

pip install -r requirements.txt


Download the Data
The primary dataset (events.csv) is ignored by .gitignore due to size. Download it from the original source and place it in the data/ folder.

Run the Jupyter Notebook
Open 1_Data_Analysis_and_Modeling.ipynb and run all cells. This generates .pkl model files and .png image assets required for the app and README.

Launch the Streamlit App

streamlit run app.py


The interactive dashboard will open in your browser.
