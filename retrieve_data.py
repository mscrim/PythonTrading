""" Functions for fetching and processing stock data
"""
import numpy as np
import pandas as pd

import pandas_datareader as pdr

from cache import simple_cache

@simple_cache
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


def include_all_weekdays(df, start_date=None, end_date=None):
    if not start_date:
        start_date = df.index.min()
    if not end_date:
        end_date = df.index.max()
    all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
    df = df.reindex(all_weekdays)
    return df

def fetch_and_process_data(start_date=None, end_date=None):
    """ Process stock data

    tickers: List
        List of stock ticker symbols to retrieve

    start_date: String
        Start date for dataset

    end_date: String
        End date for dataset

    """
    data = get_data(tickers=('sp500'), data_source='fred')
    data = include_all_weekdays(data)

    # Covert data to series
    data = data['sp500']
    data.freq = None
    return data

