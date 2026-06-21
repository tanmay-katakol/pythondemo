import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np
import os

st.set_page_config(
    page_title="Expense Tracker",
    layout="wide"
)

st.title("💰 Expense Tracker Dashboard")

EXPENSE_FILE = "expenses.csv"
COLUMNS = ["Date", "Name", "Amount", "Category"]

# ---------------- Ensure expenses file exists ----------------
if not os.path.exists(EXPENSE_FILE):
    pd.DataFrame(columns=COLUMNS).to_csv(EXPENSE_FILE, index=False, header=False)

# ---------------- Add Expense Form ----------------
st.subheader("➕ Add New Expense")

with st.form("expense_form"):

    expense_name = st.text_input("Expense Name")

    expense_amount = st.number_input(
        "Amount",
        min_value=0.0
    )

    expense_category = st.selectbox(
        "Category",
        [
            "🍔 Food",
            "🏡 Home",
            "💼 Work",
            "🎉 Fun",
            "🤷 Misc"
        ]
    )

    submitted = st.form_submit_button("Add Expense")

    if submitted:
        if not expense_name.strip():
            st.warning("Please enter an expense name.")
        else:
            new_expense = pd.DataFrame({
                "Date": [pd.Timestamp.today().date()],
                "Name": [expense_name],
                "Amount": [expense_amount],
                "Category": [expense_category]
            })

            new_expense.to_csv(
                EXPENSE_FILE,
                mode="a",
                header=False,
                index=False
            )

            st.success("Expense Added Successfully!")
            st.rerun()

# ---------------- Sidebar ----------------
st.sidebar.header("Budget Settings")

budget = st.sidebar.number_input(
    "Monthly Budget (₹)",
    min_value=0.0,
    value=2000.0,
    step=100.0
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Analytics",
        "Forecast"
    ]
)

# ---------------- Load Data ----------------
df = pd.read_csv(
    EXPENSE_FILE,
    names=COLUMNS
)

# Drop any fully empty rows just in case
df = df.dropna(how="all")

if not df.empty:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce").fillna(0.0)
else:
    df["Date"] = pd.to_datetime(pd.Series(dtype="object"))
    df["Amount"] = pd.Series(dtype="float")

# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    total_expense = df["Amount"].sum() if not df.empty else 0.0
    total_transactions = len(df)
    average_expense = df["Amount"].mean() if not df.empty else 0.0

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "💰 Total Expenses",
        f"₹{total_expense:.2f}"
    )

    col2.metric(
        "🧾 Transactions",
        total_transactions
    )

    col3.metric(
        "📊 Average Expense",
        f"₹{average_expense:.2f}" if not df.empty else "₹0.00"
    )

    col4.metric(
    "🎯 Budget",
    f"₹{budget:.0f}"
    )

    st.divider()

    if not df.empty:
        category_data = (
            df.groupby("Category")["Amount"]
            .sum()
            .reset_index()
        )

        col1, col2 = st.columns(2)

        with col1:
            fig1 = px.pie(
                category_data,
                names="Category",
                values="Amount",
                hole=0.5,
                title="Expense Distribution"
            )
            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            fig2 = px.bar(
                category_data,
                x="Category",
                y="Amount",
                title="Category Spending"
            )
            st.plotly_chart(fig2, use_container_width=True)

        st.subheader("🤖 Spending Insights")

        top_category = category_data.loc[
            category_data["Amount"].idxmax()
        ]

        st.info(
            f"Highest Spending Category: {top_category['Category']} "
            f"(₹{top_category['Amount']:.2f})"
        )

        largest_expense = df.loc[
            df["Amount"].idxmax()
        ]

        st.info(
            f"Biggest Expense: {largest_expense['Name']} "
            f"(₹{largest_expense['Amount']:.2f})"
        )
    else:
        st.info("No expenses recorded yet. Add one above to get started!")

    st.subheader("📋 Recent Transactions")

    search = st.text_input("🔍 Search Expense")

    if not df.empty:
        filtered_df = df[
            df["Name"].astype(str).str.contains(
                search,
                case=False,
                na=False
            )
        ]
    else:
        filtered_df = df

    st.dataframe(
        filtered_df.reset_index(drop=True),
        use_container_width=True
    )

    st.subheader("🗑 Delete Expense")

    if not df.empty:
        expense_index = st.number_input(
            "Enter Row Number to Delete",
            min_value=0,
            max_value=max(len(df) - 1, 0),
            step=1
        )

        if st.button("Delete Expense"):
            df = df.reset_index(drop=True)
            df = df.drop(expense_index)

            df.to_csv(
                EXPENSE_FILE,
                index=False,
                header=False
            )

            st.success("Expense Deleted Successfully!")
            st.rerun()
    else:
        st.caption("No expenses to delete.")

    st.subheader("💰 Budget Tracker")

    if budget > 0:
        budget_used = (total_expense / budget) * 100

        st.progress(min(int(budget_used), 100))

        st.write(f"Budget Used: {budget_used:.1f}%")

        st.write(f"Remaining Budget: ₹{budget - total_expense:.2f}")
    else:
        st.warning("Please enter a budget amount.")

    st.subheader("📈 Spending Trend")

    if not df.empty:
        daily_expense = (
            df.groupby("Date")["Amount"]
            .sum()
            .reset_index()
        )

        fig3 = px.line(
            daily_expense,
            x="Date",
            y="Amount",
            markers=True,
            title="Daily Spending Trend"
        )

        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.caption("No spending data to chart yet.")

    csv = df.to_csv(index=False)

    st.download_button(
        label="📥 Download Report",
        data=csv,
        file_name="expense_report.csv",
        mime="text/csv"
    )

# ---------------- ANALYTICS ----------------
elif page == "Analytics":

    st.title("📊 Analytics")

    if df.empty:
        st.info("No expenses recorded yet. Add some on the Dashboard page first!")
    else:
        top_categories = (
            df.groupby("Category")["Amount"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
        )

        st.subheader("Top Spending Categories")

        st.dataframe(top_categories)

        fig = px.bar(
            x=top_categories.values,
            y=top_categories.index,
            orientation="h",
            title="Top Categories"
        )

        st.plotly_chart(fig, use_container_width=True)

        daily_avg = (
            df.groupby("Date")["Amount"]
            .sum()
            .mean()
        )

        st.metric(
            "Average Daily Spending",
            f"₹{daily_avg:.2f}"
        )

        daily_totals = (
            df.groupby("Date")["Amount"]
            .sum()
        )

        max_day = daily_totals.idxmax()
        max_amount = daily_totals.max()

        st.metric(
            "Most Expensive Day",
            str(max_day.date()),
            f"₹{max_amount:.2f}"
        )

        fig2 = px.treemap(
            df,
            path=["Category"],
            values="Amount"
        )

        st.plotly_chart(fig2, use_container_width=True)

# ---------------- FORECAST ----------------
elif page == "Forecast":

    st.title("📈 Expense Forecast")

    daily_data = (
        df.groupby("Date")["Amount"]
        .sum()
        .reset_index()
    )

    if len(daily_data) < 2:
        st.info(
            "Not enough spending history yet to build a forecast. "
            "Add expenses on at least two different days first."
        )

    else:

        daily_data["Day_Number"] = np.arange(
            len(daily_data)
        )

        X = daily_data[["Day_Number"]]
        y = daily_data["Amount"]

        model = LinearRegression()
        model.fit(X, y)

        tomorrow = len(daily_data)

        prediction = model.predict(
            [[tomorrow]]
        )[0]

        prediction = max(prediction, 0)

        st.metric(
            "Predicted Spending Tomorrow",
            f"₹{prediction:.2f}"
        )

        st.write(
            f"Based on {len(daily_data)} days of spending data."
        )

        average_spending = daily_data["Amount"].mean()

        difference = prediction - average_spending

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Average Daily Spending",
                f"₹{average_spending:.2f}"
            )

        with col2:
            st.metric(
                "Difference From Average",
                f"₹{difference:.2f}"
            )

        if difference > 0:
            st.warning(
                "Predicted spending is above your average."
            )
        else:
            st.success(
                "Predicted spending is below your average."
            )

        st.subheader("Forecast Summary")

        if prediction > average_spending:

            st.write(
                f"Your spending is forecasted to increase by ₹{difference:.2f} tomorrow."
            )

        else:

            st.write(
                f"Your spending is forecasted to decrease by ₹{abs(difference):.2f} tomorrow."
            )

        forecast_df = daily_data.copy()

        forecast_df.loc[len(forecast_df)] = {
            "Date": pd.NaT,
            "Amount": prediction,
            "Day_Number": tomorrow
        }

        fig = px.line(
            forecast_df,
            x="Day_Number",
            y="Amount",
            markers=True,
            title="Expense Forecast Trend"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    

