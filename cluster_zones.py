import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("data/T1.csv")

features = df[['windspeed_100m', 'temperature_2m', 'Power']]

kmeans = KMeans(n_clusters=3, random_state=42)
df['Zone'] = kmeans.fit_predict(features)

zone_map = {0: "Low Zone", 1: "Medium Zone", 2: "High Zone"}
df['Zone_Label'] = df['Zone'].map(zone_map)

df.to_csv("data/wind_zones.csv", index=False)

print("Clustering Completed")
