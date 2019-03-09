import random

POSSIBLE_WEIGHTS = [0.05*n for n in range(1, 20)]

class Neural_Network:
    def __init__(self, layer_sizes, funcs):
        self._weights = {}
        layer = 1
        while layer in layer_sizes:
            self._weights[layer] = {}
            for n in range(layer_sizes[layer]):
                self._weights[layer][n] = {}
                for p in range(layer_sizes[layer -1]):
                    self._weights[layer][n][p] = random.choice(POSSIBLE_WEIGHTS)
            layer += 1
        self._funcs = funcs
        self._nets = {}
        self._error = {}
        for layer in self._weights.keys ():
            self._error[layer] = {}

    def __str__(self):
        s = ''
        for layer, weights in self._weights.items():
            s += "Layer: " + str(layer) + " Weights: " + str(weights) + '\n'
        return s

    def print_error (self):
        s = ''
        for layer, nodes in self._error.items():
            s += "Layer: " + str(layer) + " Weights: " + str(nodes) + '\n'
        return s

    def clear_error (self):
        self._error = {}
        for layer in self._weights.keys():
            self._error[layer] = {}

    def propagate (self, inputs):
        layer_outputs = inputs
        layer = 1
        while layer in self._weights.keys ():
            new_outputs = {}
            nets = {}
            for node in self._weights[layer].keys ():
                net = 0
                for previous_node in self._weights[layer][node].keys():
                    w = self._weights[layer][node][previous_node]
                    inp = w * layer_outputs[previous_node]
                    net += inp
                nets[node] = net
                new_outputs[node] = self._funcs[layer].func (net)
            self._nets[layer] = nets
            layer_outputs = new_outputs
            layer += 1
        return (layer - 1), layer_outputs

    def output_layer_error (self, output_layer, outputs, correct_outputs):
        for node in self._weights[output_layer].keys():
            delta_o = correct_outputs[node] - outputs[node]
            df_net = self._funcs[output_layer].dfunc(self._nets[output_layer][node])
            self._error[output_layer][node] = delta_o * df_net

    def hidden_layer_error(self, current_layer):
        if self._error [current_layer + 1] == {}:
            self.hidden_layer_error(current_layer + 1)
        current_layer_error = {}
        for node in self._weights[current_layer].keys():
            error_sum = 0
            for next_node in self._weights[current_layer + 1].keys():
                if self._weights[current_layer + 1][next_node] == {}:
                    print self
                    print current_layer + 1, next_node, node
                connection_w = self._weights[current_layer + 1][next_node][node]
                next_layer_node_error = self._error[current_layer + 1][next_node]
                error_sum += (connection_w * next_layer_node_error)
            df_net = self._funcs[current_layer].dfunc(self._nets[current_layer][node])
            current_layer_error[node] = df_net * error_sum
        self._error[current_layer] = current_layer_error

    def weight_update (self, inputs, n):
        layer_inputs = inputs
        layer = 1
        while layer in self._weights.keys():
            new_layer_weights = {}
            for node in self._weights[layer].keys():
                new_layer_weights[node] = {}
                for previous_node, weight in self._weights[layer][node].items ():
                    new_weight = weight + n * self._error[layer][node] * layer_inputs[previous_node]
                    new_layer_weights[node][previous_node] = new_weight
            self._weights[layer] = new_layer_weights
            #print node, self._weights[layer]
            layer_inputs = {}
            for input_node, net in self._nets[layer].items ():
                layer_inputs[input_node] = self._funcs[layer].func(net)
            layer += 1

    def back_propagation (self, inputs, outputs, n):
        self.clear_error()
        output_layer, experimental_outputs = self.propagate(inputs)
        self.output_layer_error(output_layer, experimental_outputs, outputs)
        if output_layer != 1:
            self.hidden_layer_error(1)
        self.weight_update(inputs, n)

    def error (self, inputs, outputs):
        error = 0
        dummy, results = self.propagate(inputs)
        for node, value in results:
            error += ((outputs[node] - value)**2)
        return error

    def total_trial_error (self, data):
        total_error = 0
        for pattern in data:
            inputs = pattern[0]
            outputs = pattern[1]
            e = self.error(inputs, outputs)
            total_error += e
        t_e = total_error / len (data)
        return t_e
