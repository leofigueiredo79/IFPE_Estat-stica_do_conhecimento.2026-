
import pandas as pd
import yfinance as yf

def download_data(ticker:str)-> pd.dataFrame:
    """
    download historical data.
    Args:
        ticker (str): Ticker name.
    """
    df = yf.download(
        ticker = ticker,
        multi_level_index = False
    ).reset_index()

    return df