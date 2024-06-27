# Author: Chinmay Paranjape, Kushal Kaparatti, Prathamesh Chitnis
# Version: v1.3.2
# Date: 19-JUN-2024

import math

import matplotlib.pyplot as plt


# Function to calculate number of clusters (square root of number of nodes)
def calculate_clusters(nodes):
    return math.isqrt(nodes)  # Using integer square root for cluster count

# Data
nodes = list(range(50, 1050, 50))
optimized_clusters = [calculate_clusters(n) for n in nodes]

# Plotting
plt.figure(figsize=(14, 8))
plt.plot(nodes, optimized_clusters, label='Optimized Clusters', marker='o')

plt.xlabel('Number of Nodes')
plt.ylabel('Number of Clusters')
plt.title('Number of Clusters as Number of Nodes Increases')
plt.legend()
plt.grid(True)
plt.xticks(nodes, rotation=45)
plt.tight_layout()

# Display the plot
plt.show()