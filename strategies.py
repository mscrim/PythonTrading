from datetime import timedelta

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

def buy_and_hold(d, start_date, end_date):
    """
    Buy and Hold strategy

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
    start_date = check_weekday(start_date)
    init_price = d.loc[start_date][0]
    final_price = d.loc[end_date][0]
    factor = final_price / init_price
    perc_change = (final_price - init_price) / init_price * 100.
    return factor, perc_change