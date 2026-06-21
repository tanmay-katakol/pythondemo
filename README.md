# 💰 Expense Tracker Dashboard

## 📌 Project Overview

Expense Tracker Dashboard is a Data Science project developed using Python and Streamlit. The application allows users to record daily expenses, analyze spending habits, track budgets, and forecast future spending using Machine Learning.

The project provides an interactive dashboard with visual analytics and expense forecasting to help users better manage their finances.

---

## 🚀 Features

### Expense Management

* Add new expenses
* Delete existing expenses
* Search expenses by name
* Store expenses in CSV format

### Dashboard

* Total Expenses
* Total Transactions
* Average Expense
* Budget Overview

### Data Visualization

* Expense Distribution Pie Chart
* Category-wise Spending Bar Chart
* Daily Spending Trend Graph

### Analytics

* Top Spending Categories
* Average Daily Spending
* Most Expensive Day
* Treemap Visualization

### Budget Tracking

* Monthly Budget Input
* Budget Usage Percentage
* Remaining Budget Calculation

### Machine Learning Forecast

* Linear Regression Model
* Predicts Next Day Spending
* Forecast Summary
* Forecast Trend Visualization

### Reporting

* Download Expense Report as CSV

---

## 🛠 Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Plotly Express
* Scikit-Learn

---

## 📂 Project Structure

```text
ExpenseTracker/
│
├── dashboard.py
├── expenses.csv
├── README.md
│
└── requirements.txt
```

---

## ⚙ Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd ExpenseTracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run dashboard.py
```

---

## 📊 Machine Learning Model

The forecasting module uses Linear Regression from Scikit-Learn.

Workflow:

1. Load historical expense data
2. Aggregate daily spending
3. Convert dates into numerical values
4. Train Linear Regression model
5. Predict future spending trends

---

## 🎯 Future Enhancements

* User Authentication
* Database Integration
* Expense Editing Feature
* Category Budget Alerts
* Monthly & Yearly Reports
* Advanced Forecasting Models

---

## 👨‍💻 Author

Tanmay M K

Data Science Student

---

## 📄 License

This project is developed for educational and learning purposes.
