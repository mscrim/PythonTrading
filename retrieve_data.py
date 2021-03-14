""" Functions for fetching and processing stock data
"""
import numpy as np
import pandas as pd
from functools import cache
import pandas_datareader as pdr


@cache
def get_data(tickers=('sp500'), data_source='fred', start_date=None, end_date=None):
    """ Get stock data

    tickers: Tuple
        List of stock ticker symbols to retrieve.
        Needs to be a Tuple to be hashable for @cache

    start_date: String
        Start date for dataset

    end_date: String
        End date for dataset

    """
    data = pdr.DataReader(tickers, data_source, start_date, end_date)

    return data


def include_all_weekdays(data, start_date=None, end_date=None):
    if not start_date:
        start_date = min(df.Date)
    if not end_date:
        end_date = max(df.Date)
    df.set_index('Date', inplace=True)
    close = pd.DataFrame(df['Close'])
    all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
    data = close.reindex(all_weekdays)
    return data

def process_data():
    """ Process stock data

    tickers: List
        List of stock ticker symbols to retrieve

    start_date: String
        Start date for dataset

    end_date: String
        End date for dataset

    """
    data = get_data()
    data = include_all_weekdays(data, start_date, end_date)
    return data