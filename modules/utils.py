import streamlit as st
import pandas as pd
import numpy as np

def generate_sample_data():
    sales = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=30),
        'sales': np.random.randint(2000, 7000, 30)
    })
    demand = pd.DataFrame({
        'product': ['Scissor', 'Notebook', 'Paper', 'Pin'],
        'sales_volume': np.random.randint(100, 500, 4)
    })
    stock = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=30),
        'stock_price': np.random.normal(150, 20, 30).cumsum()
    })
    churn = pd.DataFrame({
        'customer_id': range(1, 101),
        'tenure': np.random.randint(1, 10, 100),
        'total_spent': np.random.normal(1000, 300, 100),
        'churned': np.random.choice([0, 1], 100)
    })
    clv = pd.DataFrame({
        'customer_id': range(1, 101),
        'avg_purchase_value': np.random.normal(50, 10, 100),
        'purchase_frequency': np.random.normal(3, 0.5, 100),
        'clv': np.random.normal(1000, 250, 100)
    })
    return sales, demand, stock, churn, clv

def load_uploaded_csv(expected_columns):
    file = st.file_uploader("Upload CSV", type="csv")
    if file:
        df = pd.read_csv(file)
        if all(col in df.columns for col in expected_columns):
            return df
        else:
            st.error(f"CSV must contain columns: {', '.join(expected_columns)}")
            return None
    return None
