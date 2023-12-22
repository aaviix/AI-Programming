import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

# Loading the dataset from the provided CSV file
file_path = 'perceptron_dataset.csv'
df = pd.read_csv(file_path)

# Separating features and labels
X_loaded = df.iloc[:, :-1].values
y_loaded = df.iloc[:, -1].values

# Splitting the dataset into training (90%) and validation (10%) sets
X_train_loaded, X_val_loaded, y_train_loaded, y_val_loaded = train_test_split(X_loaded, y_loaded, test_size=0.1, random_state=0)

# Perceptron Algorithm with Recording
class PerceptronWithRecording:
    def __init__(self, learning_rate=0.1, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_func = self._unit_step_func
        self.weights = None
        self.bias = None

    def fit(self, X, y, X_val, y_val):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        y_ = np.array([1 if i > 0 else -1 for i in y])

        # Record accuracy after every 100 updates
        accuracy_record = {"train": [], "val": []}

        for i in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)
                update = self.lr * (y_[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update

                # Recording performance every 100 updates
                if (i * n_samples + idx) % 100 == 0:
                    train_accuracy = self.evaluate_model(X, y)
                    val_accuracy = self.evaluate_model(X_val, y_val)
                    accuracy_record["train"].append(train_accuracy)
                    accuracy_record["val"].append(val_accuracy)

        return accuracy_record

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return self.activation_func(linear_output)

    def _unit_step_func(self, x):
        return np.where(x >= 0, 1, -1)

    def evaluate_model(self, X, y):
        predictions = self.predict(X)
        accuracy = np.mean(predictions == y)
        return accuracy

# Re-using the PerceptronWithRecording class defined earlier
perceptron_loaded = PerceptronWithRecording(learning_rate=0.01, n_iters=1000)
accuracy_record_loaded = perceptron_loaded.fit(X_train_loaded, y_train_loaded, X_val_loaded, y_val_loaded)

print(accuracy_record_loaded)
