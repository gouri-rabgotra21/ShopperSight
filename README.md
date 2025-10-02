# ShopperSight: E-commerce Customer Analytics Platform

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

**You can view the live deployed application here:**
[**https://shoppersight-gp4i4axlrrsbt5dwvdcxsw.streamlit.app/**](https://shoppersight-gp4i4axlrrsbt5dwvdcxsw.streamlit.app/)

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

## Analysis & Results

### Purchase Prediction
The **Random Forest Classifier** was evaluated on a holdout test set. The confusion matrix and performance metrics indicate strong predictive capability in distinguishing "Purchased" vs. "Not Purchased" events.

### Customer Segmentation
The **K-Means algorithm** identified four customer personas:

| Cluster ID | Persona                  | Description                                                            |
|------------|--------------------------|------------------------------------------------------------------------|
| 0          | High-Value Champions     | Highly engaged, frequent purchases, top-value customers               |
| 1          | Potential Loyalists      | Moderate activity, consistent users with growth potential             |
| 2          | Window Shoppers          | High browsing activity but very few transactions                      |
| 3          | New / Infrequent Buyers  | Low engagement, likely new or occasional purchasers                   |

*Images and visualizations are generated via the notebook and used in the Streamlit dashboard.*

---

## Tech Stack

| Category             | Technologies                        |
|---------------------|------------------------------------|
| Programming Language | Python                             |
| Libraries            | Pandas, NumPy, Scikit-learn, Joblib |
| Web Framework        | Streamlit                          |
| Visualization        | Matplotlib, Seaborn                |
| Tools                | Jupyter Notebook, VS Code, Git     |

---

## Setup and Installation

### Clone the Repository
```bash
git clone https://github.com/gouri-rabgotra21/ShopperSight.git
cd ShopperSight

---

