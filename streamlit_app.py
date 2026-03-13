import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/housing.csv")

st.title("Housing Market Analysis Dashboard")

st.subheader("Dataset Overview")
st.write(data.head())

st.subheader("House Price Distribution")

fig, ax = plt.subplots()
sns.histplot(data["median_house_value"], bins=50, kde=True, ax=ax)
st.pyplot(fig)

st.subheader("Median Income vs House Price")

fig, ax = plt.subplots()
sns.scatterplot(x="median_income", y="median_house_value", data=data, alpha=0.3, ax=ax)
st.pyplot(fig)

st.subheader("House Price by Ocean Proximity")

fig, ax = plt.subplots()
sns.boxplot(x="ocean_proximity", y="median_house_value", data=data, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)
