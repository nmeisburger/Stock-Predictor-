import math

def sigmoid (x):
    ex1 = math.exp(-x)
    ex2 = ex1 + 1
    ex3 = 1 / ex2
    return ex3

def sigmoid_derivative (x):
    ex1 = math.exp(-x)
    ex2 = ex1 + 1
    ex3 = ex2 ** 2
    ex4 = ex1 / ex3
    return ex4

class Activation_Function:
    def __init__(self, function, dfunction):
        self.func = function
        self.dfunc = dfunction