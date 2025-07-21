import streamlit as st
import plotly.express as px
from sklearn.linear_model import LinearRegression
from modules.utils import load_uploaded_csv

def clv_prediction(default):
    st.subheader("Customer Lifetime Value Prediction")
    uploaded_data = load_uploaded_csv(['avg_purchase_value', 'purchase_frequency', 'clv'])
    data = uploaded_data if uploaded_data is not None else default
    st.write(data.head())
    X = data[['avg_purchase_value', 'purchase_frequency']]
    y = data['clv']
    model = LinearRegression()
    model.fit(X, y)
    prediction = model.predict(X)
    data['predicted_clv'] = prediction
    fig = px.scatter(data, x='avg_purchase_value', y='predicted_clv', title="Predicted CLV vs Purchase Value")
    st.plotly_chart(fig)
