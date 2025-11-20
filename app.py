import streamlit as st
import pandas as pd
import plotly.express as px


# Load cleaned data
data = pd.read_csv('../data/water_quality_cleaned.csv')


st.title('Water Quality Dashboard')


# KPIs
st.header('Key Indicators')
st.metric('Average pH', round(data['ph'].mean(), 2))
st.metric('Average Hardness', round(data['Hardness'].mean(), 2))
st.metric('Average Solids', round(data['Solids'].mean(), 2))


# Feature visualization
st.header('Feature Trends')
feature = st.selectbox('Select feature to visualize', data.columns[:-1])
fig = px.histogram(data, x=feature)
st.plotly_chart(fig)


# Potability counts
st.header('Water Potability')
potability_counts = data['Potability'].value_counts()
fig2 = px.bar(x=potability_counts.index, y=potability_counts.values, labels={'x':'Potability','y':'Count'})
st.plotly_chart(fig2)
