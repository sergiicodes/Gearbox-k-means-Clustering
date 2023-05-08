import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

location = r"Analyzer Selection2.xlsx"
excel = pd.read_excel(location, sheet_name="GBX DATABASE", skiprows=1)

df = pd.DataFrame(excel)

# Check the column names in your DataFrame
print(df.columns)

# Extract the features you want to cluster on
features = df[['Ratio', 'Cost']]  # The columns from the read Excel

# Calculate the within-cluster sum of squares (WCSS) for different values of k
wcss = []
k_values = np.arange(1, 13, 1)  # Essentially the x-tick setting (format: min, max, x-tick value)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)

# Plot the elbow curve
plt.plot(k_values, wcss)
plt.title('Elbow Curve')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.xticks(k_values)
plt.show()
