import pandas as pd
import matplotlib.pyplot as plt

data = {
    'temperature': [60, 70, 80, 90, 100],
    'vibration': [1, 2, 3, 4, 5],
    'pressure': [30, 35, 40, 45, 50],
    'failure': [0, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

print(df)

# Graph 1
plt.scatter(df['temperature'], df['failure'])
plt.xlabel("Temperature")
plt.ylabel("Failure")
plt.title("Temperature vs Failure")
plt.show()

# Graph 2
plt.scatter(df['vibration'], df['failure'])
plt.xlabel("Vibration")
plt.ylabel("Failure")
plt.title("Vibration vs Failure")
plt.show()

# Graph 3
plt.scatter(df['pressure'], df['failure'])
plt.xlabel("Pressure")
plt.ylabel("Failure")
plt.title("Pressure vs Failure")
plt.show()
