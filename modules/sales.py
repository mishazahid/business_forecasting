import streamlit as st
import plotly.express as px
from modules.utils import load_uploaded_csv
import pandas as pd
from prophet import Prophet

def sales_forecasting(default):
    st.subheader("Sales Forecasting")

    # Step 1: Load data
    uploaded_data = load_uploaded_csv(['date', 'sales'])
    data = uploaded_data if uploaded_data is not None else default
    data['date'] = pd.to_datetime(data['date'])
    st.write("Raw Data:", data.head())

    # Step 2: Plot actual sales
    fig = px.line(data, x='date', y='sales', title="Historical Sales")
    st.plotly_chart(fig)

    # Step 3: Prepare data for Prophet
    df_prophet = data.rename(columns={'date': 'ds', 'sales': 'y'})
    
    # Step 4: Fit Prophet model
    model = Prophet()
    model.fit(df_prophet)

    # Step 5: Create future dataframe (e.g., 30 days ahead)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    # Step 6: Plot forecast
    fig_forecast = px.line(forecast, x='ds', y='yhat', title='Sales Forecast (Next 30 Days)')
    fig_forecast.add_scatter(x=data['date'], y=data['sales'], mode='lines', name='Actual Sales')
    st.plotly_chart(fig_forecast)
