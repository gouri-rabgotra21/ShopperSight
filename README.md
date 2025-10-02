# ShopperSight: E-commerce Customer Analytics Platform

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents
1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Dashboard Preview](#dashboard-preview)
4. [Project Workflow](#project-workflow)
5. [Analysis & Results](#analysis--results)
6. [Tech Stack](#tech-stack)
7. [Local Installation](#setup-and-local-installation)

---

## Overview

ShopperSight is an end-to-end data science project that analyzes a large-scale e-commerce dataset (over 2.7 million events) to derive actionable business insights. The project features a supervised machine learning model to predict customer purchase intent and an unsupervised clustering model to segment shoppers into distinct behavioral groups. The entire pipeline, from data processing to prediction, is showcased through a user-friendly, interactive web dashboard built with Streamlit.

This project serves as a comprehensive demonstration of a typical data science workflow, including data cleaning, feature engineering, model training, evaluation, and the deployment of a proof-of-concept data product.

---

## Key Features

* **Purchase Likelihood Prediction:** A Random Forest Classifier is trained to predict the probability of a user event leading to a transaction, a key metric for enhancing personalization and marketing efforts.
* **Customer Segmentation:** K-Means clustering is implemented to segment customers who have made purchases into distinct behavioral groups, allowing for targeted business strategies.
* **Interactive Web Dashboard:** A web application built with Streamlit provides a user-friendly interface to perform live predictions and explore the customer segments.

---

## Dashboard Preview

*A preview of the live, interactive dashboard built with Streamlit.*

![ShopperSight Dashboard](image_53d62e.jpg) 
*Note: Make sure this image file is pushed to your GitHub repository.*

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
The Random Forest model was evaluated on a held-out test set. The confusion matrix below visualizes its performance in distinguishing between "Purchased" and "Not Purchased" events.

Note: Make sure this image file is created by your notebook and pushed to your GitHub repository.

2. Customer Segment Analysis
The K-Means algorithm identified four distinct customer personas based on their browsing and transaction behavior.

Cluster ID	Persona	Characteristics
0	High-Value Champions	High number of views, add-to-carts, and transactions. These are the most engaged and valuable customers.
1	Potential Loyalists	Moderate activity across the board. They are consistent but have room to grow into Champions.
2	Window Shoppers	Very high number of views but a very low number of transactions. They browse a lot but rarely buy.
3	New / Infrequent Buyers	Low activity in all metrics. Likely new customers or those who purchase rarely.

Of course. It looks like the formatting was lost in the previous message.

Here is the complete, properly formatted code for your advanced README.md file. It is all in a single block so you can copy it once.

Important Reminder: Before you paste this, please remember to add the plt.savefig(...) lines to your notebook and re-run it to create the confusion_matrix.png and segment_analysis.png files, as mentioned in the previous message.

README Code (All-in-One)
Markdown

# ShopperSight: E-commerce Customer Analytics Platform

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents
1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Dashboard Preview](#dashboard-preview)
4. [Project Workflow](#project-workflow)
5. [Analysis & Results](#analysis--results)
6. [Tech Stack](#tech-stack)
7. [Local Installation](#setup-and-local-installation)

---

## Overview

ShopperSight is an end-to-end data science project that analyzes a large-scale e-commerce dataset (over 2.7 million events) to derive actionable business insights. The project features a supervised machine learning model to predict customer purchase intent and an unsupervised clustering model to segment shoppers into distinct behavioral groups. The entire pipeline, from data processing to prediction, is showcased through a user-friendly, interactive web dashboard built with Streamlit.

This project serves as a comprehensive demonstration of a typical data science workflow, including data cleaning, feature engineering, model training, evaluation, and the deployment of a proof-of-concept data product.

---

## Key Features

* **Purchase Likelihood Prediction:** A Random Forest Classifier is trained to predict the probability of a user event leading to a transaction, a key metric for enhancing personalization and marketing efforts.
* **Customer Segmentation:** K-Means clustering is implemented to segment customers who have made purchases into distinct behavioral groups, allowing for targeted business strategies.
* **Interactive Web Dashboard:** A web application built with Streamlit provides a user-friendly interface to perform live predictions and explore the customer segments.

---

## Dashboard Preview

*A preview of the live, interactive dashboard built with Streamlit.*

![ShopperSight Dashboard](image_53d62e.jpg) 
*Note: Make sure this image file is pushed to your GitHub repository.*

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
The Random Forest model was evaluated on a held-out test set. The confusion matrix below visualizes its performance in distinguishing between "Purchased" and "Not Purchased" events.

Note: Make sure this image file is created by your notebook and pushed to your GitHub repository.

2. Customer Segment Analysis
The K-Means algorithm identified four distinct customer personas based on their browsing and transaction behavior.

Cluster ID	Persona	Characteristics
0	High-Value Champions	High number of views, add-to-carts, and transactions. These are the most engaged and valuable customers.
1	Potential Loyalists	Moderate activity across the board. They are consistent but have room to grow into Champions.
2	Window Shoppers	Very high number of views but a very low number of transactions. They browse a lot but rarely buy.
3	New / Infrequent Buyers	Low activity in all metrics. Likely new customers or those who purchase rarely.
Note: Make sure this image file is created by your notebook and pushed to your GitHub repository.

Tech Stack
Category	Technologies
Programming Language	Python
Core Libraries	Pandas, NumPy, Scikit-learn, Joblib
Web Framework	Streamlit
Data Visualization	Matplotlib, Seaborn
Development Tools	VS Code, Jupyter Notebooks, Git, GitHub
Of course. It looks like the formatting was lost in the previous message.

Here is the complete, properly formatted code for your advanced README.md file. It is all in a single block so you can copy it once.

Important Reminder: Before you paste this, please remember to add the plt.savefig(...) lines to your notebook and re-run it to create the confusion_matrix.png and segment_analysis.png files, as mentioned in the previous message.

README Code (All-in-One)
Markdown

# ShopperSight: E-commerce Customer Analytics Platform

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents
1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Dashboard Preview](#dashboard-preview)
4. [Project Workflow](#project-workflow)
5. [Analysis & Results](#analysis--results)
6. [Tech Stack](#tech-stack)
7. [Local Installation](#setup-and-local-installation)

---

## Overview

ShopperSight is an end-to-end data science project that analyzes a large-scale e-commerce dataset (over 2.7 million events) to derive actionable business insights. The project features a supervised machine learning model to predict customer purchase intent and an unsupervised clustering model to segment shoppers into distinct behavioral groups. The entire pipeline, from data processing to prediction, is showcased through a user-friendly, interactive web dashboard built with Streamlit.

This project serves as a comprehensive demonstration of a typical data science workflow, including data cleaning, feature engineering, model training, evaluation, and the deployment of a proof-of-concept data product.

---

## Key Features

* **Purchase Likelihood Prediction:** A Random Forest Classifier is trained to predict the probability of a user event leading to a transaction, a key metric for enhancing personalization and marketing efforts.
* **Customer Segmentation:** K-Means clustering is implemented to segment customers who have made purchases into distinct behavioral groups, allowing for targeted business strategies.
* **Interactive Web Dashboard:** A web application built with Streamlit provides a user-friendly interface to perform live predictions and explore the customer segments.

---

## Dashboard Preview

*A preview of the live, interactive dashboard built with Streamlit.*

![ShopperSight Dashboard](image_53d62e.jpg) 
*Note: Make sure this image file is pushed to your GitHub repository.*

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
The Random Forest model was evaluated on a held-out test set. The confusion matrix below visualizes its performance in distinguishing between "Purchased" and "Not Purchased" events.

Note: Make sure this image file is created by your notebook and pushed to your GitHub repository.

2. Customer Segment Analysis
The K-Means algorithm identified four distinct customer personas based on their browsing and transaction behavior.

Cluster ID	Persona	Characteristics
0	High-Value Champions	High number of views, add-to-carts, and transactions. These are the most engaged and valuable customers.
1	Potential Loyalists	Moderate activity across the board. They are consistent but have room to grow into Champions.
2	Window Shoppers	Very high number of views but a very low number of transactions. They browse a lot but rarely buy.
3	New / Infrequent Buyers	Low activity in all metrics. Likely new customers or those who purchase rarely.
Note: Make sure this image file is created by your notebook and pushed to your GitHub repository.

Tech Stack
Category	Technologies
Programming Language	Python
Core Libraries	Pandas, NumPy, Scikit-learn, Joblib
Web Framework	Streamlit
Data Visualization	Matplotlib, Seaborn
Development Tools	VS Code, Jupyter Notebooks, Git, GitHub
Setup and Local Installation
To run this project on your local machine, please follow the steps below.

1. Clone the Repository

Bash

git clone [https://github.com/gouri-rabgotra21/ShopperSight.git](https://github.com/gouri-rabgotra21/ShopperSight.git)
cd ShopperSight
2. Install Dependencies
(It is recommended to use a virtual environment)

Bash

pip install -r requirements.txt
3. Download the Data
The primary dataset (events.csv) is ignored by .gitignore due to its size. Please download it from its original source and place it inside a data/ folder.

4. Run the Jupyter Notebook
Open 1_Data_Analysis_and_Modeling.ipynb and run all cells. This is crucial as it generates the model files (.pkl) and image assets (.png) needed for the app and README.

5. Launch the Streamlit App

Bash

streamlit run app.py
The interactive dashboard will open in your browser.

License
This project is licensed under the MIT License.


