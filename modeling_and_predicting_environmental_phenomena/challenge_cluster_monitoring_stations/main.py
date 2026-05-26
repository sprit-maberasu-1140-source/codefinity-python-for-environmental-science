import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = {
    "Station": ["North", "South", "East", "West", "Central", "SuburbA", "SuburbB", "Industrial", "Park", "Airport"],
    "NO2": [32, 45, 28, 55, 38, 22, 25, 70, 18, 60],
    "SO2": [12, 20, 9, 25, 15, 8, 10, 30, 7, 22],
    "PM10": [40, 55, 35, 65, 48, 30, 33, 80, 28, 70]
}
df = pd.DataFrame(data)

# Select pollutant columns for clustering
X = df[["NO2", "SO2", "PM10"]]

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)

# Plot NO2 vs PM10, color by cluster, label points
plt.figure(figsize=(8, 6))
for cluster in sorted(df["Cluster"].unique()):
    cluster_data = df[df["Cluster"] == cluster]
    plt.scatter(cluster_data["NO2"], cluster_data["PM10"], label=f"Cluster {cluster}")
for _, row in df.iterrows():
    plt.text(row["NO2"] + 0.5, row["PM10"] + 0.5, row["Station"], fontsize=8)
plt.xlabel("NO₂ (µg/m³)")
plt.ylabel("PM10 (µg/m³)")
plt.title("Monitoring Stations Clustered by Pollutant Levels")
plt.legend()
plt.show()