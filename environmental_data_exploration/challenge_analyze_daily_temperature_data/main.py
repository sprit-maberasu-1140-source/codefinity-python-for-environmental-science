import pandas as pd

df = pd.DataFrame({
    "date": pd.to_datetime([
        "2023-01-01", "2023-01-02", "2023-01-03",
        "2023-01-04", "2023-01-05", "2023-01-06",
        "2023-01-07"
    ]),
    "temperature_C": [5.2, 6.1, 4.8, 7.3, 3.9, 8.0, 2.5]
})

# Calculate summary statistics
average_temp = df["temperature_C"].mean()
min_temp = df["temperature_C"].min()
max_temp = df["temperature_C"].max()

# Find days with minimum and maximum temperature
coldest_days = df[df["temperature_C"] == min_temp]
hottest_days = df[df["temperature_C"] == max_temp]

# Print summary
print(f"Yearly Temperature Summary:")
print(f"- Average: {average_temp:.2f}°C")
print(f"- Minimum: {min_temp:.2f}°C on {', '.join(coldest_days['date'].dt.strftime('%Y-%m-%d'))}")
print(f"- Maximum: {max_temp:.2f}°C on {', '.join(hottest_days['date'].dt.strftime('%Y-%m-%d'))}")