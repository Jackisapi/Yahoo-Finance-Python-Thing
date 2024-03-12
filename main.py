import streamlit as st
from datetime import date
import yahoo_man as yh
import file_functions as ff

st.title("Stock Price Analysis")

ticker_id = st.text_input("Enter ticker (for example LHM ")
while ticker_id == '':
    continue


s_date = st.text_input("Please enter a date YYYY-MM-DD ")


e_date = str(date.today())

st.write(f"Loading Data {ticker_id}")

yh.download_data(ticker=ticker_id, start_date=s_date, end_date=e_date)

data = ff.file_formatter_from_file()

st.write(data)