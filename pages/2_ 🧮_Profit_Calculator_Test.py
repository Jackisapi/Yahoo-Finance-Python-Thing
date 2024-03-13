import time

import streamlit as st
import yahoo_man as yh
import file_functions as ff
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
st.title("Profit Calculator")

ticker_id = st.text_input("Enter ticker (for example AMD)")

s_date = st.text_input("Please enter a start date (YYYY-MM-DD Format)")

e_date = st.text_input("Please enter a end date (YYYY-MM-DD Format)")
while ticker_id == '':
    continue
st.write(f"Loading Data {ticker_id}")

yh.download_data(ticker=ticker_id, start_date=s_date, end_date=e_date)
data = ff.file_formatter_from_file()

option = st.selectbox(
    "Where would you like to make your profit calculation?",
    ('', 'Open', 'High', 'Low', 'Close', 'Adj Close')
)
while option == '':
    continue
if option == 'Open':
    invest_cost = float(data.iloc[0]['Open'])
    current_cost = float(data.iloc[len(data) - 1]['Open'])
    profit = round(current_cost - invest_cost, 2)
    st.subheader(f"Your profit is {profit}")
elif option == 'High':
    invest_cost = float(data.iloc[0]['High'])
    current_cost = float(data.iloc[len(data) - 1]['High'])
    profit = round(current_cost - invest_cost, 2)
    st.subheader(f"Your profit is {profit} Per Share")
elif option == 'Low':
    invest_cost = float(data.iloc[0]['Low'])
    current_cost = float(data.iloc[len(data) - 1]['Low'])
    profit = round(current_cost - invest_cost, 2)
    st.subheader(f"Your profit is {profit}Per Share")
elif option == 'Close':
    invest_cost = float(data.iloc[0]['Close'])
    current_cost = float(data.iloc[len(data) - 1]['Close'])
    profit = round(current_cost - invest_cost, 2)
    st.subheader(f"Your profit is {profit} Per Share")
elif option == 'Adj Close':
    invest_cost = float(data.iloc[0]['Close'])
    current_cost = float(data.iloc[len(data) - 1]['Close'])
    profit = round(current_cost - invest_cost, 2)
    st.subheader(f"Your profit is {profit} Per Share")

share_amount = st.number_input("How many shares do you have?")
while share_amount == '':
    continue
st.subheader(f"You earned {profit * share_amount} Before Taxes and whatnot")