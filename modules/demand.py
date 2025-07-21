import streamlit as st
import numpy as np
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor
from modules.utils import load_uploaded_csv
import pandas as pd

def demand_prediction(default):
    st.subheader("Demand Prediction")
    uploaded_data = load_uploaded_csv(['product', 'sales_volume'])
    data = uploaded_data if uploaded_data is not None else default
    st.write(data)
    X = data[['sales_volume']]
    y = np.random.normal(100, 10, len(data))
    model = RandomForestRegressor()
    model.fit(X, y)
    prediction = model.predict(X)
    fig = px.bar(data, x='product', y=prediction, labels={'y': 'Predicted Demand'})
    st.plotly_chart(fig)
