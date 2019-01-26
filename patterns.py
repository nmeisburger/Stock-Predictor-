import json

def read_file (filename):
    file = open(filename)
    file_string = file.read()
    file_data = json.loads(file_string)
    return file_data

def make_patterns ():
    dates = read_file('dates.txt')
    dataset = read_file('normalizeddata.txt')
    macd_data = dataset['macd']
    rsi_data = dataset['RSI']
    spy_data = dataset['SPY']
    percent_data = dataset['percent_change']
    ema_data = dataset['EMA']
    cci_data = dataset['CCI']
    outputs = read_file('normalizedoutputs.txt')
    final_dataset = {}
    for i in range(len(dates) - 10):
        day = dates[i + 5]
        macd = macd_data[i]
        rsi = rsi_data[i]
        spy = spy_data[i]
        percent = percent_data[i]
        ema = ema_data[i]
        cci = cci_data[i]
        final_dataset[day] = ({0: macd, 1: rsi, 2: spy, 3: percent, 4: ema, 5: cci}, {0: outputs[i]})
    return final_dataset

def write_data (data, file):
    data_file = open(file, 'w')
    json_data = json.dumps(data)
    data_file.write(json_data)
    data_file.close()
    return None

patterns = make_patterns()

write_data(patterns, 'patterns.txt')