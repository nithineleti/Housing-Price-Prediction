# House Price Prediction Model

This project implements a house price prediction model using statistical analysis and machine learning techniques. The model uses the California Housing dataset to predict median house values based on various features.

## Project Overview

The project uses StatsModels and Scikit-learn to build a regression model for predicting house prices. It includes data exploration, preprocessing, model training, and evaluation steps.

## Dependencies

- Python 3.x
- pandas
- matplotlib
- seaborn
- statsmodels
- scikit-learn
- numpy

## Dataset

The project uses the California Housing dataset (`housing.csv`) which includes the following features:
- Median income
- Housing features
- Geographic information
- Median house values (target variable)

## Project Structure

The project is organized into several key tasks:

1. Data Import and Setup
2. Dataset Loading and Initial Exploration
3. Data Exploration and Analysis
4. Null Value Handling
5. Data Preparation and Feature Engineering
6. Model Training using StatsModels OLS
7. Model Evaluation and Visualization

## Key Features

- Comprehensive data exploration and visualization
- Feature engineering with one-hot encoding
- Statistical modeling using OLS (Ordinary Least Squares)
- Model performance visualization
- Mean Squared Error evaluation

## Visualizations

The project includes several visualizations:
- Correlation analysis between features
- Linear correlation between median income and house values
- Prediction vs actual value comparison plots

## Model Performance

The model's performance is evaluated using:
- Statistical summary from StatsModels
- Mean Squared Error metrics
- Visual comparison of predicted vs actual values

## Getting Started

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter notebook `Statsmodel.ipynb`

## Results

The model provides insights into housing price predictions with visualizations showing the relationship between actual and predicted values. The implementation includes statistical analysis to understand feature importance and model performance.

## License

This project is open-source and available under the MIT License.
# Housing-Price-Prediction
