import pandas as pd
import matplotlib.pyplot as plt

data = {
    "date": pd.date_range(start="2024-06-01", periods=14, freq="D"),
    "aqi": [75, 82, 95, 110, 120, 99, 85, 102, 130, 88, 92, 105, 97, 115]
}
df = pd.DataFrame(data)

threshold = 100
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["aqi"], label="AQI", color="blue", marker="o")
exceed = df["aqi"] > threshold
plt.scatter(df["date"][exceed], df["aqi"][exceed], color="red", label="AQI > 100", zorder=5)
plt.title("Daily Air Quality Index (AQI) Trends")
plt.xlabel("Date")
plt.ylabel("AQI Value")
plt.legend()
plt.tight_layout()
plt.show()
