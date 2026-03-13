# Housing Market Data Analysis & House Price Prediction

This project analyzes housing market data and builds a regression model to predict house prices using statistical and machine learning techniques. The analysis is based on the **California Housing dataset** and focuses on identifying the key factors that influence housing prices.

The project demonstrates **data analysis, visualization, statistical modeling, and business insight generation**, making it suitable for **Data Analyst and Data Science portfolio projects**.

---

# Project Overview

The goal of this project is to analyze housing market trends and predict median house values based on multiple features such as income, location, population, and housing characteristics.

The project includes:

* Data exploration and cleaning
* Exploratory Data Analysis (EDA)
* Statistical modeling using **StatsModels OLS regression**
* Machine learning workflow using **Scikit-learn**
* Data visualization and interpretation
* Model performance evaluation

---

# Dataset

The project uses the **California Housing dataset (`housing.csv`)**.

### Features in the dataset:

* Longitude
* Latitude
* Housing Median Age
* Total Rooms
* Total Bedrooms
* Population
* Households
* Median Income
* Ocean Proximity
* Median House Value (Target Variable)

---

# Project Workflow

The analysis follows these main steps:

1. Import Libraries and Setup Environment
2. Load and Explore the Dataset
3. Data Cleaning and Null Value Handling
4. Exploratory Data Analysis (EDA)
5. Correlation Analysis Between Features
6. Feature Engineering and Encoding
7. Train-Test Data Splitting
8. Linear Regression Modeling using StatsModels
9. Model Evaluation and Prediction Visualization
10. Business Insight Generation

---

# Exploratory Data Analysis

Several visualizations were created to understand the dataset and identify important relationships between variables.

### Distribution of House Prices

Shows the overall distribution of median house values.

### Correlation Heatmap

Analyzes relationships between all numerical features.

### Ocean Proximity vs House Price

Compares housing prices across different geographic locations.

### Median Income vs House Price

Shows the strong relationship between income levels and property values.

### Average House Price by Location

Summarizes pricing trends based on proximity to the ocean.

### Geographic Housing Price Map

Visualizes the geographic distribution of housing prices using latitude and longitude.

### Population vs House Price

Examines whether population density affects property prices.

---

## Business Questions

This project explores the housing dataset to answer several key business questions related to real estate pricing:

* What factors influence house prices the most?
* Do houses located near the ocean have higher prices?
* How does median income affect housing prices?
* Does population density influence property value?
* How does geographic location impact housing prices?

These questions guide the exploratory data analysis and help derive insights that can support data-driven decision-making in the housing market.


# Key Insights

The analysis revealed several important insights:

* **Median income is the strongest predictor of housing prices.**
* Houses located **near the ocean generally have higher prices**.
* **Inland houses have lower average housing prices.**
* Geographic location significantly affects property values.
* Population has a weaker relationship with housing prices compared to income.

These insights highlight the importance of **economic and geographic factors** in determining housing market trends.

---

# Model Implementation

The regression model was implemented using **StatsModels Ordinary Least Squares (OLS)**.

### Model Steps

1. Feature preparation and one-hot encoding
2. Train-test data split
3. OLS regression model training
4. Model summary interpretation
5. Prediction generation
6. Model performance evaluation

---

# Model Evaluation

Model performance was evaluated using:

* **StatsModels statistical summary**
* **Mean Squared Error (MSE)**
* **Root Mean Squared Error (RMSE)**
* **R² Score**

Visual comparisons between **actual and predicted house prices** were also created to assess model accuracy.

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* StatsModels
* Scikit-learn
* Jupyter Notebook

---

# Project Structure

```
Housing-Price-Prediction
│
├── data
│   └── housing.csv
│
├── notebooks
│   └── housing_market_data_analysis.ipynb
│
├── images
│   └── visualizations
│
├── sql
│   └── housing_analysis.sql
│
├── requirements.txt
│
└── README.md
```

---

# Skills Demonstrated

This project demonstrates the following **Data Analyst skills**:

* Data Cleaning
* Exploratory Data Analysis
* Data Visualization
* Statistical Modeling
* Regression Analysis
* Feature Engineering
* Model Evaluation
* Business Insight Generation

---

# Getting Started

### 1. Clone the repository

```
git clone https://github.com/yourusername/Housing-Price-Prediction.git
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the notebook

Open and run:

```
housing_market_data_analysis.ipynb
```

---

# Results

The project successfully demonstrates how statistical analysis and machine learning can be used to understand housing market trends and predict house prices. The insights obtained from this analysis can help support **data-driven decision-making in real estate markets**.

---

# Author

**Nithin Pious**

---

# License

This project is open-source and available under the **MIT License**.
