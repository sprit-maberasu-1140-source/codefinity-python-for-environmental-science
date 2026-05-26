import pandas as pd
from scipy import stats

# Create DataFrames with at least 8 PM2.5 measurements each
df_x = pd.DataFrame({'PM2.5': [23, 25, 22, 24, 26, 27, 24, 25]})
df_y = pd.DataFrame({'PM2.5': [30, 29, 31, 32, 28, 30, 29, 31]})

# Perform independent two-sample t-test
t_stat, p_value = stats.ttest_ind(df_x['PM2.5'], df_y['PM2.5'])

# Print results
print("T-statistic:", t_stat)
print("P-value:", p_value)

# Interpretation
if p_value < 0.05:
    print("There is a statistically significant difference in PM2.5 levels between the two stations.")
else:
    print("There is no statistically significant difference in PM2.5 levels between the two stations.")