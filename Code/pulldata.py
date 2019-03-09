import datarequests
import json

def generate_dates (start_month, end_month, year):
    dates = []
    for month in range(start_month, end_month + 1):
        for day in range (1,32):
            date = str(year) + '-'
            if month < 10:
                date += '0' + str(month) + '-'
            else:
                date += str(month) + '-'
            if day < 10:
                date += '0' + str(day)
            else:
                date += str(day)
            dates.append(date)
    return dates

def preceding_change (stock, dates_used):
    daily_closes = datarequests.get_daily_close(stock)
    sub_changes = []
    for j in range(5, len(dates_used) - 5):
        start = float(daily_closes[dates_used[j - 5]]["4. close"])
        end = float(daily_closes[dates_used[j]]["4. close"])
        change = (end - start) / start
        sub_changes.append(change)
    return sub_changes

def compile_data (stock):
    macd = datarequests.get_macd(stock)
    datarequests.time_delay(10)
    print "MACD\n"
    rsi = datarequests.get_rsi(stock)
    datarequests.time_delay(10)
    print "RSI\n"
    ema = datarequests.get_ema(stock)
    datarequests.time_delay(10)
    print "EMA\n"
    cci = datarequests.get_cci(stock)
    datarequests.time_delay(10)
    print "CCI\n"
    d1 = generate_dates(11, 12, 2018)
    d2 = generate_dates(1, 1, 2019)
    dates = d1 + d2

    data = {}
    dates_used = []
    macd_data = []
    rsi_data = []
    ema_data = []
    cci_data = []
    for date in dates:
        if date in macd.keys ():
            dates_used.append(date)
            macdd = float(macd[date]["MACD_Hist"])
            macd_data.append(macdd)
            rsid = float(rsi[date]["RSI"])
            rsi_data.append(rsid)
            emad = float(ema[date]["EMA"])
            ema_data.append(emad)
            ccid = float(cci[date]["CCI"])
            cci_data.append(ccid)
    data["macd"] = macd_data[5:-5]
    data["RSI"] = rsi_data[5:-5]
    data["EMA"] = ema_data[5:-5]
    data["CCI"] = cci_data[5:-5]
    return dates_used, data

def output_data (stock, dates_used):
    daily_closes = datarequests.get_daily_close(stock)
    sub_changes = []
    for j in range(len(dates_used) - 5):
        start = float(daily_closes[dates_used[j + 1]]["4. close"])
        end = float(daily_closes[dates_used[j + 5]]["4. close"])
        change = (end - start) / start
        sub_changes.append(change)
    return sub_changes

def write_data (data, file):
    data_file = open(file, 'w')
    json_data = json.dumps(data)
    data_file.write(json_data)
    data_file.close()
    return None

def read_file (filename):
    file = open(filename)
    file_string = file.read()
    file_data = json.loads(file_string)
    return file_data

SYMBOL = 'AMZN'

dates, data = compile_data(SYMBOL)

spy_data = preceding_change('SPY', dates)
percent_data = preceding_change(SYMBOL, dates)

data['SPY'] = spy_data

data['percent_change'] = percent_data

write_data(data, 'jsondata.txt')
write_data(dates, 'dates.txt')

outputs = output_data(SYMBOL, dates)

write_data(outputs, 'outputs.txt')
