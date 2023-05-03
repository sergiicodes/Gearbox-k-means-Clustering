# Gearbox Analysis Project

This project focuses on the analysis and visualization of gearbox data—specifically, how brand and gearbox ratio relates to pricing. It involves performing tasks such as data exploration, k-means clustering, visualization, and analysis of gearbox brand names.

## Files

- `elbow_curve.py`: This script calculates the within-cluster sum of squares (WCSS) for different values of k and plots the elbow curve. It helps determine the optimal number of clusters (k) for the k-means clustering algorithm.
![elbow_curve](https://user-images.githubusercontent.com/79073281/236025771-3b2bdf5f-040f-4c55-bd7b-9f357e2b3039.png)

- `k_means_cluster.py`: This script performs k-means clustering on the gearbox data based on the optimal k-value obtained from the elbow curve analysis. It assigns cluster labels to the data points, visualizes the clusters using scatter plots, and adds interactivity by displaying gearbox names on click.

![k-mean](https://user-images.githubusercontent.com/79073281/236025895-5a70bb36-6429-4a0b-bce7-da89f3f1d9dc.png)

- `gbx_report.py`: This script analyzes specific columns of the gearbox data. It calculates the mode (most common value) and occurrence count for the first three letters of each column, representing gearbox brand names.

## Usage

1. Install the required dependencies: pandas, matplotlib, scikit-learn, mplcursors.

