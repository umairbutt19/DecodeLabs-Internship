import pandas as pd
import math
from collections import Counter


# Load dataset
df = pd.read_csv("iris.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nClass distribution:")
print(df["species"].value_counts())


# Convert class names into numbers
class_mapping = {
    "setosa": 0,
    "versicolor": 1,
    "virginica": 2
}

df["target"] = df["species"].map(class_mapping)


# Select features
features = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width"
]

X = df[features].values.tolist()
y = df["target"].tolist()


# Split dataset into training and testing data
split_index = int(len(df) * 0.8)

X_train = X[:split_index]
y_train = y[:split_index]

X_test = X[split_index:]
y_test = y[split_index:]


print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# Calculate Euclidean distance
def euclidean_distance(point1, point2):
    distance = 0

    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2

    return math.sqrt(distance)


# KNN classification
def predict_knn(test_point, X_train, y_train, k=5):
    distances = []

    for i in range(len(X_train)):
        distance = euclidean_distance(test_point, X_train[i])
        distances.append((distance, y_train[i]))

    distances.sort()

    nearest_neighbors = distances[:k]

    neighbor_classes = []

    for distance, label in nearest_neighbors:
        neighbor_classes.append(label)

    prediction = Counter(neighbor_classes).most_common(1)[0][0]

    return prediction


# Make predictions
predictions = []

for test_point in X_test:
    prediction = predict_knn(test_point, X_train, y_train)
    predictions.append(prediction)


# Calculate accuracy
correct_predictions = 0

for actual, predicted in zip(y_test, predictions):
    if actual == predicted:
        correct_predictions += 1

accuracy = correct_predictions / len(y_test)

print("\nModel Accuracy:")
print(f"{accuracy:.2%}")


# Display predictions
label_mapping = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

print("\nPredictions:")

for i in range(len(y_test)):
    actual = label_mapping[y_test[i]]
    predicted = label_mapping[predictions[i]]

    print(
        f"Actual: {actual:<12} "
        f"Predicted: {predicted}"
    )