import pandas as pd


data = {
    'temperature': [60, 70, 80, 90, 100],
    'vibration': [1, 2, 3, 4, 5],
    'pressure': [30, 35, 40, 45, 50],
    'failure': [0, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

print(df)
