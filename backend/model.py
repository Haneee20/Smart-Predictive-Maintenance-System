import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Dataset
data = {
    'temperature': [60, 70, 80, 90, 100, 65, 75, 85, 95, 105],
    'vibration': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'pressure': [30, 35, 40, 45, 50, 32, 36, 42, 48, 52],
    'failure': [0, 0, 0, 1, 1, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

# Features & target
X = df[['temperature', 'vibration', 'pressure']]
y = df['failure']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Prediction function (IMPORTANT)
def predict(temperature, vibration, pressure):
    input_data = [[temperature, vibration, pressure]]
    result = model.predict(input_data)
    return result[0]
