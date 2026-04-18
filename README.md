# House Price Prediction using Machine Learning

## Overview
This project demonstrates a machine learning approach to predicting house prices using regression techniques. A synthetic dataset was generated based on multiple housing features to simulate real-world conditions.

---

## Dataset
- The dataset is **synthetically generated** using the following features:
  - Area
  - Number of Bedrooms
  - House Age
  - Distance from city center

- Target variable (Price) was calculated using a custom formula with added random noise:
  
  Price = (Area * 0.03 + Bedrooms * 5 - House_Age * 0.7 - Distance * 1.5 + noise)

- Noise was added using a normal distribution to simulate real-world variation.

---

## Exploratory Data Analysis (EDA)
- Analyzed relationships between features and price
- Observed strong correlation between Area and Price
- Visualized feature impact using plots and heatmaps

---

## Data Preprocessing
- Checked for missing values
- Feature scaling (if applied)
- Train-test split

---

## Model Building
- Applied Linear Regression model
- Trained on synthetic dataset
- Learned relationships between input features and price

---

## Model Performance
- **R² Score:** 0.91  
- **RMSE:** 10.06  
- **MSE:** 101.27  

The high R² score is expected as the data follows a defined mathematical relationship with controlled noise.

---

## Visualizations
- Correlation Heatmap  
- Feature vs Price plots  
- Predicted vs Actual comparison  

---

## Tech Stack
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  

---

## Key Learning
- Understanding regression modeling
- Impact of features on prediction
- Effect of noise in data
- Model evaluation using R², RMSE, MSE

---

## Future Improvements
- Use real-world datasets (e.g., housing market data)
- Apply advanced models (Random Forest, XGBoost)
- Deploy using Streamlit or Flask

---

## Author
Aishwarya Bandgar  
