import requests
import time

API_KEY = 'HR4KT0A4PW6IDERF'

def get_macd (stock):
    parameters = {'function': 'MACD', 'symbol': stock, 'interval': 'daily', 'series_type': 'close', 'apikey': API_KEY}
    response = requests.get('https://www.alphavantage.co/query?', params=parameters)
    return response.json()["Technical Analysis: MACD"]

def get_rsi (stock):
    parameters = {'function': 'RSI', 'symbol': stock, 'interval': 'daily', 'time_period': 60,
                      'series_type': 'close', 'apikey': API_KEY}
    response = requests.get('https://www.alphavantage.co/query?', params=parameters)
    return response.json()["Technical Analysis: RSI"]

def get_bbands (stock):
    parameters = {'function': 'BBANDS', 'symbol': stock, 'interval': 'daily', 'time_period': 60,
                      'series_type': 'close', 'apikey': API_KEY}
    response = requests.get('https://www.alphavantage.co/query?', params=parameters)
    return response.json()["Technical Analysis: BBANDS"]

def get_ema (stock):
    parameters = {'function': 'EMA', 'symbol': stock, 'interval': 'daily', 'time_period': 60,
                      'series_type': 'close', 'apikey': API_KEY}
    response = requests.get('https://www.alphavantage.co/query?', params=parameters)
    return response.json()["Technical Analysis: EMA"]

def get_cci (stock):
    parameters = {'function': 'CCI', 'symbol': stock, 'interval': 'daily', 'time_period': 60, 'apikey': API_KEY}
    response = requests.get('https://www.alphavantage.co/query?', params=parameters)
    return response.json()["Technical Analysis: CCI"]

def get_daily_close (stock):
    parameters = {'function': 'TIME_SERIES_DAILY', 'symbol': stock, 'apikey': API_KEY}
    response = requests.get('https://www.alphavantage.co/query?', params=parameters)
    return response.json()["Time Series (Daily)"]

def time_delay (duration):
    time.sleep(duration)