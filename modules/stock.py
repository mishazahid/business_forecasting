import streamlit as st
import numpy as np
import plotly.express as px
import xgboost as xgb
from modules.utils import load_uploaded_csv
import pandas as pd

def stock_prediction(default):
    st.subheader("Stock Price Prediction")
    uploaded_data = load_uploaded_csv(['date', 'stock_price'])
    data = uploaded_data if uploaded_data is not None else default
    data['date'] = pd.to_datetime(data['date'])
    X = np.array(range(len(data))).reshape(-1, 1)
    y = data['stock_price'].values
    model = xgb.XGBRegressor()
    model.fit(X, y)
    prediction = model.predict(X)
    data['predicted'] = prediction
    fig = px.line(data, x='date', y=['stock_price', 'predicted'], title="Actual vs Predicted Stock Price")
    st.plotly_chart(fig)
