import streamlit as st
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor
from modules.utils import load_uploaded_csv

def churn_prediction(default):
    st.subheader("Churn Prediction")
    uploaded_data = load_uploaded_csv(['tenure', 'total_spent', 'churned'])
    data = uploaded_data if uploaded_data is not None else default
    st.write(data.head())
    X = data[['tenure', 'total_spent']]
    y = data['churned']
    model = RandomForestRegressor()
    model.fit(X, y)
    prediction = model.predict(X)
    data['predicted_churn'] = prediction
    fig = px.histogram(data, x='predicted_churn', nbins=20, title="Churn Probability Distribution")
    st.plotly_chart(fig)
