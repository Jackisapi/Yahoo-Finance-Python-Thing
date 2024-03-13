import streamlit as st
from datetime import date
import yahoo_man as yh
import file_functions as ff

st.title("Stock Price Analysis")

ticker_id = st.text_input("Enter ticker (for example AMD)")
while ticker_id == '':
    continue

s_date = st.text_input("Please enter a date (YYYY-MM-DD Format)")
while s_date == '':
    continue

# ticker_id = 'AMD'
# s_date = '2018-06-14'

e_date = str(date.today())

st.write(f"Loading Data {ticker_id}")

yh.download_data(ticker=ticker_id, start_date=s_date, end_date=e_date)

data = ff.file_formatter_from_file()

st.write(data)

chart = st.line_chart(data=data, x="Date", y=('Open', 'High', 'Low'), width=10000, use_container_width=True)
