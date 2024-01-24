#Implement stochastic gradient descent for a sigmoidal perceptron and compare its performance with that of the thresholded perceptron.
## Author : 22200727

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load and prepare data
file_path = 'perceptron_dataset.csv'
df = pd.read_csv(file_path)

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.1, random_state=0)

# Base Perceptron class for common functionalities
class BasePerceptron:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def _initialize_weights(self, n_features):
        self.weights = np.zeros(n_features)
        self.bias = 0

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return self.activation_func(linear_output)

    def evaluate_model(self, X, y):
        predictions = self.predict(X)
        return np.mean(predictions == y)


class ThresholdedPerceptron(BasePerceptron):
    def __init__(self, learning_rate=0.01, n_iters=1000):
        super().__init__(learning_rate, n_iters)
        self.activation_func = lambda x: np.where(x >= 0, 1, -1)

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self._initialize_weights(n_features)

        y_adjusted = np.array([1 if i > 0 else -1 for i in y])

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)
                update = self.lr * (y_adjusted[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update


class SigmoidalPerceptron(BasePerceptron):
    def __init__(self, learning_rate=0.01, n_iters=1000):
        super().__init__(learning_rate, n_iters)
        self.activation_func = lambda x: 1 / (1 + np.exp(-x))

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self._initialize_weights(n_features)

        y_adjusted = np.array([1 if i > 0 else 0 for i in y])

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)
                update = self.lr * (y_adjusted[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        probabilities = super().predict(X)
        return np.where(probabilities > 0.5, 1, 0)


# Train and evaluate models
thresholded_perceptron = ThresholdedPerceptron(learning_rate=0.01, n_iters=1000)
thresholded_perceptron.fit(X_train, y_train)
thresholded_accuracy = thresholded_perceptron.evaluate_model(X_val, y_val)

sigmoidal_perceptron = SigmoidalPerceptron(learning_rate=0.01, n_iters=1000)
sigmoidal_perceptron.fit(X_train, y_train)
sigmoidal_accuracy = sigmoidal_perceptron.evaluate_model(X_val, y_val)

print("Thresholded Perceptron Validation Accuracy:", thresholded_accuracy)
print("Sigmoidal Perceptron Validation Accuracy:", sigmoidal_accuracy)
