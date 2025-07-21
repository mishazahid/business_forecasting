# 📊 Ironclad Analytics

**Ironclad Analytics** is an interactive, Streamlit-based data analytics dashboard that provides key predictive insights for business metrics like sales, demand, churn, and customer lifetime value (CLV). Built using machine learning models and Plotly for rich visualizations, this app supports both sample and user-uploaded CSV data for real-time predictions.

---

## 🚀 Features

🔹 **Sales Forecasting**
Uses Prophet to forecast future sales trends based on historical data.

🔹 **Demand Prediction**
Estimates product demand using Random Forests trained on sales volume.

🔹 **Churn Prediction**
Predicts customer churn probabilities using customer behavior features.

🔹 **Customer Lifetime Value (CLV)**
Estimates CLV using linear regression on purchase behavior metrics.

🔹 **Custom CSV Uploads**
Upload your own data in any tab to get tailored predictions instantly.

---

## 🧪 Technologies Used

* **Streamlit**: Interactive web app framework
* **Plotly Express**: Dynamic, interactive plots
* **Prophet**: Time series forecasting
* **scikit-learn**: Machine learning models
* **pandas / numpy**: Data wrangling & manipulation

---

## 📁 Folder Structure

```
├── app.py
├── modules/
│   ├── churn.py
│   ├── clv.py
│   ├── demand.py
│   ├── sales.py
│   └── utils.py
├── assets/
│   └── logo.png
├── requirements.txt
└── README.md
```

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/mishazahid/business_forecasting.git
cd business_forecasting
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501`.

---

## 📤 Using Your Own Data

Each module allows CSV uploads with required column headers:

| Module            | Required Columns                                  |
| ----------------- | ------------------------------------------------- |
| Sales Forecasting | `date`, `sales`                                   |
| Demand Prediction | `product`, `sales_volume`                         |
| Churn Prediction  | `tenure`, `total_spent`, `churned`                |
| CLV Prediction    | `avg_purchase_value`, `purchase_frequency`, `clv` |

Make sure your uploaded CSV matches the expected format.

---

## 🧠 Future Enhancements

* Add Stock Price Forecasting
* Model accuracy metrics
* Downloadable reports
* Support for more complex input formats

---

## 📌 License

This project is licensed under the MIT License. Feel free to use and adapt it for personal or commercial projects.

---

## 🙌 Acknowledgements

* Streamlit Team
* Facebook Prophet
* scikit-learn contributors
* Plotly community

