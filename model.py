import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data
data = pd.read_csv("data/sensor_data.csv")

X = data.drop("failure", axis=1)
y = data["failure"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")
