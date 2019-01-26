import network
import activationfunctions
import json
import matplotlib.pyplot as plt

def read_file (filename):
    file = open(filename)
    file_string = file.read()
    file_data = json.loads(file_string)
    return file_data

def denormalize (val, min_val, max_val):
    delta = max_val - min_val
    return val * delta + min_val

architecture = {0:6, 1:6, 2:3, 3:1}

sigmoid = activationfunctions.Activation_Function(activationfunctions.sigmoid, activationfunctions.sigmoid_derivative)

afuncs = {1: sigmoid, 2: sigmoid, 3: sigmoid}

network = network.Neural_Network(architecture, afuncs)

MIN_MAX = read_file('minmax.txt')

def train (n_val):
    data = read_file('patterns.txt')
    dates = read_file('dates.txt')
    for n in range(-45, -35):
        pattern = data[dates[n + 5]]
        converted_inputs = {}
        inputs = pattern[0]
        for key, val in inputs.items():
            converted_inputs[int(key)] = val
        outputs = pattern[1]
        converted_outputs = {}
        for key1, val1 in outputs.items():
            converted_outputs[int(key1)] = val1
        network.back_propagation(converted_inputs, converted_outputs, n_val)
        print network


def test ():
    data = read_file('patterns.txt')
    dates = read_file('dates.txt')
    predictions = []
    actuals = []
    for n in range(-35, -5):
        pattern = data[dates[n]]
        converted_inputs = {}
        inputs = pattern[0]
        for key, val in inputs.items():
            converted_inputs[int(key)] = val
        outputs = pattern[1]
        converted_outputs = {}
        for key1, val1 in outputs.items():
            converted_outputs[int(key1)] = val1
        dummy, result = network.propagate(converted_inputs)
        prediction = denormalize(result[0], MIN_MAX[0], MIN_MAX[1])
        actual = denormalize(converted_outputs[0], MIN_MAX[0], MIN_MAX[1])
        predictions.append(prediction)
        actuals.append(actual)
        print 'Prediction:', prediction, 'Actual:', actual
    return predictions, actuals


train(2)

g1, g2 = test()

day = range(1,31)

plt.plot(day, g1, color='blue')
#plt.plot(day, g2, color='red')
plt.xlabel('Day')
plt.ylabel('% change over next 5 days')
plt.title('AMZN')
plt.show ()




