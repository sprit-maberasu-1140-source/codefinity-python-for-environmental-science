import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame: daily rainfall for one year
# (You do not need to change this data)
data = {
    "date": pd.date_range(start="2023-01-01", end="2023-12-31", freq="D"),
    # 31-pattern * 11 + first 24 to get 365 elements
    "rainfall_mm": [2, 0, 0, 5, 1, 0, 3, 0, 0, 2, 0, 1, 0, 0, 4, 0, 0, 3, 0, 0, 2, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0]*11
                   + [2, 0, 0, 5, 1, 0, 3, 0, 0, 2, 0, 1, 0, 0, 4, 0, 0, 3, 0, 0, 2, 0, 0, 1]
}
df = pd.DataFrame(data)

def analyze_monthly_rainfall(df):
    # Add a month column with calendar month names
    df["month"] = df["date"].dt.strftime("%B")
    
    # Group by month and sum rainfall
    monthly_rainfall = df.groupby("month")["rainfall_mm"].sum()
    
    # Ensure months are in calendar order
    months_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    monthly_rainfall = monthly_rainfall.reindex(months_order)
    
    # Identify highest and lowest rainfall months
    max_month = monthly_rainfall.idxmax()
    min_month = monthly_rainfall.idxmin()
    
    # Print totals and highlight max/min
    print("Total monthly rainfall (mm):")
    print(monthly_rainfall)
    print(f"\nMonth with highest rainfall: {max_month} ({monthly_rainfall[max_month]} mm)")
    print(f"Month with lowest rainfall: {min_month} ({monthly_rainfall[min_month]} mm)")
    
    # Plot bar chart
    plt.figure(figsize=(10, 5))
    monthly_rainfall.plot(kind="bar", color="skyblue")
    plt.title("Total Monthly Rainfall")
    plt.xlabel("Month")
    plt.ylabel("Rainfall (mm)")
    plt.tight_layout()
    plt.show()

analyze_monthly_rainfall(df)