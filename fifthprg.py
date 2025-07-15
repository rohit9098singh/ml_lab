import pandas as pd
import matplotlib.pyplot as plt

data = {'x': [10, 20, 30, 40], 'y': [100, 200, 300, 400]}
df = pd.DataFrame(data)

# Bar Chart
plt.figure(1)
plt.bar(df['x'], df['y'])
plt.title("Bar Chart using Matplotlib")
plt.xlabel("X")
plt.ylabel("Y")

# Scatter Plot
plt.figure(2)
plt.scatter(df['x'], df['y'], color='green')
plt.title("Scatter Plot using Matplotlib")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
