import streamlit as st
from modules.sales import sales_forecasting
from modules.demand import demand_prediction
from modules.stock import stock_prediction
from modules.churn import churn_prediction
from modules.clv import clv_prediction
from modules.utils import generate_sample_data

# Page Config
st.set_page_config(page_title="Ironclad Analytics", page_icon="📊", layout="wide")

st.sidebar.image("assets/logo.png", width=110)
st.markdown("<h1 style='text-align: center; color: #F5F5F5;'>Ironclad Analytics</h1><br><br>", unsafe_allow_html=True)
st.sidebar.markdown("📂 Upload a CSV in the active tab to use your own data")

def main():
    sales, demand, stock, churn, clv = generate_sample_data()
    tab = st.sidebar.radio("Choose Analysis", [
        "Sales Forecasting",
        "Demand Prediction",
        #"Stock Prediction",
        "Churn Prediction",
        "CLV Prediction"
    ])
    if tab == "Sales Forecasting":
        sales_forecasting(sales)
    elif tab == "Demand Prediction":
        demand_prediction(demand)
    elif tab == "Stock Prediction":
        stock_prediction(stock)
    elif tab == "Churn Prediction":
        churn_prediction(churn)
    elif tab == "CLV Prediction":
        clv_prediction(clv)

if __name__ == "__main__":
    main()
