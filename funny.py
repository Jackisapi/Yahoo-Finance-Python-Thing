import yfinance as yf
import pandas as pd
def set_ticker(ticker_id):
    try:
        ticker = yf.Ticker(ticker_id)
        # Initializes the Ticker from Yahoo Finance
        ticker_data = (ticker_id,ticker)
        #Sets the Ticker Name and the Ticker into a tuple (find better solution later) and returns
        return ticker_data


    except Exception as e:
        print(f"Yo dawg i tried to get ticker {ticker_id} but i couldnt find it this be whi \n {e}")

def num_formatter(column_name,file):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    for i in range(0,len(file)):
        file.loc[i,column_name] = round(float(file.loc[i,column_name]),2)
    return file


def file_formatter(file_name='data.csv',write=False):
    file = pd.read_csv(file_name)
    for column in file.columns:
        try:
            num_formatter(column_name=column,file=file)
        except ValueError:
            continue
    if write == True:
        file.to_csv('data.csv')
        return file
    else:
        return file

