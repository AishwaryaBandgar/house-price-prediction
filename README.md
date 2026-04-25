# House Price Prediction using Machine Learning

## Overview
This project predicts house prices based on features such as area, number of bedrooms, house age, and distance from the city center.

A Linear Regression model is used, and the dataset is synthetically generated for learning and demonstration purposes.

 ## Features
Exploratory Data Analysis (EDA)
Feature relationship visualization
Linear Regression model training
Model evaluation (MAE, R² Score)
Interactive web app using Streamlit

## Model Performance
- **R² Score:** 0.91  
- **RMSE:** 10.06  
- **MSE:** 101.27  

The high R² score is expected as the data follows a defined mathematical relationship with controlled noise.

## Tech Stack
Python  
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib

## Model Details
Algorithm: Linear Regression
Input Features:
    Area
    Bedrooms
    House Age
    Distance
Target
    Price

## Installation and Setup
1. Clone the repository
git clone https://github.com/AishwaryaBandgar/house-price-analysis.git
cd house-price-analysis

3. Install dependencies
pip install -r requirements.txt

5. Run the Streamlit app
streamlit run app.py

## Note
This project uses a synthetic dataset, so results may not reflect real-world housing prices.

## Future Improvements
Use real-world datasets
Try advanced models (Random Forest, XGBoost)
Deploy the app online

## Author
Aishwarya Bandgar  

---
