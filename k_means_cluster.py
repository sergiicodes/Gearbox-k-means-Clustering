import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import mplcursors

location = r"C:\Users\shacosta\Desktop\Analyzer Selection2.xlsx"
excel = pd.read_excel(location, sheet_name="GBX DATABASE", skiprows=1)

df = pd.DataFrame(excel)

# Extract the features you want to cluster on
features = df[['Ratio', 'Cost']]

# Set the number of clusters (k) based on the optimal k-number from the elbow curve
k = 3  # Replace with your optimal k-number

# Perform k-means clustering
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(features)
labels = kmeans.labels_

# Add the cluster labels to the DataFrame
df['Cluster'] = labels

# Define custom colors for the clusters
colors = ['red', 'green', 'blue']

# Define custom price range names for the legend
price_ranges = ['Price-Efficient', 'Price-Moderate', 'Price-Premium']

# Visualize the clusters
fig, ax = plt.subplots()
scatter = []
for cluster in range(k):
    cluster_data = df[df['Cluster'] == cluster]
    scatter.append(ax.scatter(cluster_data['Ratio'], cluster_data['Cost'], color=colors[cluster], label=price_ranges[cluster]))

# Add the gearbox name annotations on click
cursor = mplcursors.cursor(scatter)

@cursor.connect("add")
def on_add(sel):
    index = sel.target.index
    description = df.loc[index, 'Description']
    sel.annotation.set_text(description)

plt.grid(True)
plt.xlabel("Ratio")
plt.ylabel("Price")
plt.legend()
plt.title("Gearbox Ratio vs. Cost")

plt.show()
