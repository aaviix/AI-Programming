#Author: 22200727

import numpy as np
from sympy import symbols, exp

def linear_activation(weights, inputs):
    return sum(w * x for w, x in zip(weights, inputs))

def sigmoid_activation(weights, inputs):
    z = sum(w * x for w, x in zip(weights, inputs))
    return 1 / (exp(-z) + 1)

class Perceptron:
    def __init__(self, num_inputs, activation_func, weights=None):
        self.num_inputs = num_inputs
        self.activation_func = activation_func
        self.weights = np.random.random(num_inputs + 1) - 0.5 if weights is None else np.array(weights)

    def output(self, inputs):
        inputs = np.array([1] + inputs)  # Adding 1 for the bias term
        return self.activation_func(self.weights, inputs)

    def loss(self, dataset):
        return sum((target - self.output(inputs)) ** 2 for inputs, target in dataset) / 2

    def train(self, dataset, max_epochs=100000, batch_size=20, learning_rate=1e-3):
        for epoch in range(max_epochs):
            for _ in range(batch_size):
                index = np.random.randint(len(dataset))
                inputs, target = dataset[index]
                inputs = np.array([1] + inputs)  # Adding 1 for the bias term
                output = self.output(inputs)
                error = target - output
                gradients = -error * np.array([diff(self.activation_func(self.weights, inputs), self.weights[i]) for i in range(self.num_inputs + 1)])
                self.weights -= learning_rate * gradients

            if epoch % 10 == 0:
                print(f"Epoch {epoch}: Loss = {self.loss(dataset)}")

# Generate synthetic training data
np.random.seed(42)
training_data = [(np.random.rand(2), np.random.rand()) for _ in range(100)]

# Initialize perceptrons
linear_perceptron = Perceptron(2, linear_activation)
sigmoid_perceptron = Perceptron(2, sigmoid_activation)

# Train perceptrons
print("Training Linear Perceptron")
linear_perceptron.train(training_data)
print("\nTraining Sigmoid Perceptron")
sigmoid_perceptron.train(training_data)
