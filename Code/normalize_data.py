import json

def normalize (data):
    normalized_data = []
    min_val = min (data)
    max_val = max(data)
    delta = max_val - min_val
    for n in data:
        s = (n - min_val) / delta
        normalized_data.append(s)
    return normalized_data

def normalize_outputs (data):
    normalized_data = []
    min_val = min (data)
    max_val = max(data)
    delta = max_val - min_val
    for n in data:
        s = (n - min_val) / delta
        normalized_data.append(s)
    return normalized_data, (min_val, max_val)

def read_file (filename):
    file = open(filename)
    file_string = file.read()
    file_data = json.loads(file_string)
    return file_data

def write_data (data, file):
    data_file = open(file, 'w')
    json_data = json.dumps(data)
    data_file.write(json_data)
    data_file.close()
    return None

def normalize_data ():
    new_data = {}
    data_vals = read_file('jsondata.txt')
    for type, values in data_vals.items ():
        new_values = normalize(values)
        new_data[type] = new_values
    write_data(new_data, 'normalizeddata.txt')
    return None

def normalize_output_data ():
    data_vals = read_file('outputs.txt')
    new_values, min_max = normalize_outputs(data_vals)
    write_data(new_values, 'normalizedoutputs.txt')
    write_data(min_max, 'minmax.txt')
    return None

def denormalize (val, min_val, max_val):
    delta = max_val - min_val
    return val * delta + min_val

def make_patterns ():
    dates = read_file('dates.txt')
    dataset = read_file('normalizeddata.txt')
    macd_data = dataset['macd']
    rsi_data = dataset['RSI']
    spy_data = dataset['SPY']
    percent_data = dataset['percent_change']
    ema_data = dataset['EMA']
    cci_data = dataset['CCI']

    final_dataset = {}
    for i in range(len(dates)):
        day = dates[i]
        macd = macd_data[i]
        rsi = rsi_data[i]
        spy = spy_data[i]
        percent = percent_data[i]
        ema = ema_data[i]
        cci = cci_data[i]
        final_dataset[day] = {0: macd, 1: rsi, 2: spy, 3: percent, 4: ema, 5: cci}
    return final_dataset


normalize_data()
normalize_output_data()
