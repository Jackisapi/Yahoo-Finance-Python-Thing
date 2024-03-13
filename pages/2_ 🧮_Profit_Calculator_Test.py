import streamlit as  st
import yahoo_man as yh
import file_functions as ff
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
st.title("Profit Calculator")


ticker_id = 'AMD'
s_date = '2018-06-14'

e_date = '2023-06-14'
st.write(f"Loading Data {ticker_id}")

yh.download_data(ticker=ticker_id, start_date=s_date, end_date=e_date)
data = ff.file_formatter_from_file()

st.write(data.iloc[0])
st.write(data.iloc[len(data)-1])