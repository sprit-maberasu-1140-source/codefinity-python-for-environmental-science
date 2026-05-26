import pandas as pd

# Sample environmental data: daily temperature (°C) and humidity (%)
data = {
    "temperature": [22, 24, 19, 23, 25, 27, 21, 26, 28, 20, 22, 24, 23, 25],
    "humidity": [55, 50, 60, 53, 48, 45, 58, 47, 44, 62, 56, 51, 54, 49]
}
df = pd.DataFrame(data)

# Compute the correlation coefficient
correlation = df["temperature"].corr(df["humidity"])

# Determine strength
if correlation >= 0.7 or correlation <= -0.7:
    strength = "strong"
elif correlation >= 0.3 or correlation <= -0.3:
    strength = "weak"
else:
    strength = "no"

# Determine direction
if correlation > 0:
    direction = "positive"
elif correlation < 0:
    direction = "negative"
else:
    direction = "no"

print(round(correlation, 2))  # print the rounded correlation coefficient

if strength == "no":
    print("There is no correlation between temperature and humidity.")
else:
    print(f"There is a {strength} {direction} correlation between temperature and humidity.")