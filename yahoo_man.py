import yfinance as yf
import json


def set_ticker(ticker_id):
    try:
        ticker = yf.Ticker(ticker_id)
        # Initializes the Ticker from Yahoo Finance
        ticker_data = (ticker_id, ticker)
        # Sets the Ticker Name and the Ticker into a tuple (find better solution later) and returns
        return ticker_data
    except Exception as e:
        print(f"Yo dog this failed {e}")


def download_data(ticker, file_name='data.csv', start_date='2020-01-01', end_date='2020-02-02'):
    #Takes a ticker a start and end Date as Parameters  and downloads it as a csv
    yf.download(ticker, start=start_date, end=end_date).to_csv(file_name)


def company_data(ticker, write=False):
    data = yf.Ticker(ticker).get_info()
    #Fetches company data from the ticker
    if write:
        #if write is true writes to a json file (mostly for debug stuff)
        with open(f'{ticker}.json', 'w') as outfile:
            json.dump(data, outfile)
    return data


def company_data_formatter(ticker):
    data = company_data(ticker)
    return (f"Company Name: {ticker} \n"
            f"Company Location:\n"
            f"   Country: {data['country']} \n"
            f"    City Name: {data['city']} \n"
            f"    Address: {data['address1']}\n"
            f"    ZIP: {data['zip']}")

