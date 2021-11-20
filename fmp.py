# TODO: DRAFT

# External Imports
import pandas as pd
import requests
import logging
from ratelimit import limits, sleep_and_retry
from arctic import Arctic

# External Imports
from alpacaMetadata import loa
from config import base_url, api_key

logging.basicConfig(filename='logs/data.log', filemode='a', format='%(asctime)s %(name)s - %(levelname)s - %(message)s')
# 300 calls per minute
calls = 300
rate_limit = 60


@sleep_and_retry
@limits(calls=calls, period=rate_limit)
def check_limit():
    # Empty function to throttle calls to API
    return None


# TODO: No handling of existing data, etc yet. Just naive grab of datya for symbol, also no "last working day handling etc, which is in old prokect

def api_get_data(ticker, start_date, end_date):
    """ Makes API calls to grab daily historic prices, cleans, and returns dataframe"""
    # API Call
    str_start_date = str(start_date)
    str_end_date = str(end_date)

    url = base_url + "historical-price-full/" + ticker + "?from=" + str_start_date + "&to=" + str_end_date + "&apikey=" \
          + api_key
    response = requests.get(url)
    j = response.json()

    # Clean response
    try:
        data = pd.DataFrame.from_dict(j['historical'])
    except KeyError:
        logging.error('%s failed to pull_data ticker from API ', ticker)
        print(ticker, "failed")
        pass
    data.drop(['label', 'changeOverTime', 'changePercent'], axis=1, inplace=True)
    data.set_index('date', inplace=True)
    data.sort_index(ascending=True, inplace=True)
    print(ticker, "success")
    return data


# Handle errors outside of the class below - not functioning
class localDB:
    def __init__(self, database: str):
        self.database = database

    def write(self, database, column_name):
        store = Arctic('localhost')
        write_library = store[self]
        write_library.write(data, column_name)


if __name__ == "__main__":
    for asset in loa:
        ticker = asset.symbol
        print(ticker)
        # Grab data from API
        new_data = api_get_data(ticker, "2000-01-01", "2021-11-19")
        # Write to local DB naively (overwrite, no append etc)
        localDB.write('US_ALPACA', new_data, ticker)
