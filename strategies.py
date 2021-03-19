from datetime import timedelta
import matplotlib.pyplot as plt

from strategy import TradingStrategy

def check_weekday(start_date):
    """ 
    Check that start_date is a weekday. If not, set it to the
    following Monday.

    Inputs
    ----------
    start_date : pd.Timestamp

    Returns
    -------
    start_date : pd.Timestamp

    """
    weekday_no = start_date.weekday()
    if weekday_no == 5: # Saturday
        start_date = start_date + timedelta(days=2)
    if weekday_no == 6: # Sunday
        start_date = start_date + timedelta(days=1)
    return start_date

class buy_and_hold(TradingStrategy):

    def __init__(self, data, start_date, end_date):
        self.data = data
        self.start_date = check_weekday(start_date)
        self.end_date = end_date

    def returns(self):
        """
        Inputs
        ----------
        d : pd.Series
            Daily prices for a single stock ticker
        start_date : pd.Timestamp
            Start date for the strategy
        end_date : pd.Timestamp
            End date for the strategy

        Returns
        -------
        returns : pd.Series
            Return vs date
        """
        d = self.data
        init_price = d.loc[self.start_date]
        returns = d / init_price
        return returns

    def end_returns(d):
        """
        Calculate returns as of end_date

        Inputs
        ----------
        d : pd.Series
            Daily prices for a single stock ticker
        start_date : pd.Timestamp
            Start date for the strategy
        end_date : pd.Timestamp
            End date for the strategy

        Returns
        -------
        factor : float
            Factor by which initial investment changes
        perc_change : float
            Percentage by which initial investment changes
        """
        #start_date = check_weekday(start_date)
        init_price = d.loc[self.start_date][0]
        final_price = d.loc[self.end_date][0]
        factor = final_price / init_price
        perc_change = (final_price - init_price) / init_price * 100.
        return factor, perc_change



    