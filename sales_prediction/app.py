
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE

# Page title
st.title("📊 Sales Prediction Based on Advertisement Spending")

# Load dataset
st.subheader("Dataset Preview")
df = pd.read_csv("ads.csv", index_col=0)
st.dataframe(df.head())

# Data statistics
st.subheader("Descriptive Statistics")
st.dataframe(df.describe())

# Pairplot
st.subheader("Pairplot of Features")
st.markdown("Visualizing pairwise relationships in the dataset.")
sns.pairplot(df, diag_kind='kde')
st.pyplot(plt.gcf())
plt.clf()

# Heatmap
st.subheader("Correlation Heatmap")
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
st.pyplot(plt.gcf())
plt.clf()

# Feature Selection using RFE
st.subheader("Recursive Feature Elimination (RFE)")
X = df.drop('sales', axis=1)
y = df['sales']
model = LinearRegression()
rfe = RFE(estimator=model, n_features_to_select=1)
fit = rfe.fit(X, y)

# Displaying RFE results
st.write("**Feature Ranking:**", fit.ranking_)
st.write("**Selected Feature:**", list(X.columns[fit.support_]))
