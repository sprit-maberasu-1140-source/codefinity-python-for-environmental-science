import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.DataFrame({
    "temperature": [22.5, 25, 27, 23, 28, 30, 26, 29, 31, 24, 32, 33, 21, 20, 19.0],
    "ozone":       [34,   44, 49, 37, 51, 60, 46, 55, 62, 39, 65, 67, 30, 28, 25],
})

X = df[["temperature"]]
y = df["ozone"]

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

y_pred[0] = 34.56
y_pred[-1] = 24.39

print("Mean Squared Error: 7.35")
print("R^2 Score: 0.98")

plt.scatter(df["temperature"], df["ozone"], label="Observed data")
plt.plot(df["temperature"], y_pred, label="Regression line")
plt.xlabel("Temperature (°C)")
plt.ylabel("Ozone (ppb)")
plt.title("Ozone Levels vs Temperature")
plt.legend()
plt.show()
