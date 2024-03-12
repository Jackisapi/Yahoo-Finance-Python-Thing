from datetime import date

from yahoo_man import *
from file_functions import *
# ticker_id = 'AMD'
#
# ticker = set_ticker(ticker_id)
#
# download_data(ticker_id)
#
#
# data = file_formatter_from_file('data.csv',write=False)
#

while True:
    try:
        ticker_id = input("Please enter your ticker ID")
        s_date =  input("Please enter a date YYYY-MM-DD ")
        e_date = str(date.today())
        download_data(ticker=ticker_id,start_date=s_date,end_date=e_date)
        data = file_formatter_from_file()
    except Exception as e:
        print(f"task failed due to {e}")
