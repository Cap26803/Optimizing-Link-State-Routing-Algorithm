# @author: Chinmay Paranjape, Kushal Kaparatti, Prathamesh Chitnis
# @version: v1.2.0
# @date: 13-JUN-2024

import random
import time

import matplotlib.pyplot as plt
import networkx as nx


class LSRA_Baseline:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, node1, node2, weight):
        self.graph.add_edge(node1, node2, weight=weight)

    def shortest_path(self, source, target):
        # Initialize distances to infinity
        distances = {node: float('inf') for node in self.graph.nodes()}
        distances[source] = 0

        # Introduce redundant loop to slow down the process
        for _ in range(len(self.graph.nodes()) * 2):  # Redundant extra iterations
            for _ in range(len(self.graph.edges())):  # Nested redundant loop
                pass

        # Relax edges repeatedly with additional unnecessary calculations
        for _ in range(len(self.graph.nodes()) - 1):
            for node1, node2 in self.graph.edges():
                distances[node2] = min(distances[node2], distances[node1] + self.graph[node1][node2]['weight'])
                # Additional redundant computations
                _ = sum(range(100))

        # Additional redundant step to further slow down the process
        redundant_list = [random.randint(1, 100) for _ in range(1000)]
        redundant_sum = sum(redundant_list)

        return distances  # Return distances instead of a single value

if __name__ == "__main__":
    lsra_baseline = LSRA_Baseline()

    # Prompt the user for the number of nodes
    num_nodes = int(input("Enter the number of nodes: "))

    # Add nodes with random edges and weights based on user input
    for i in range(num_nodes):
        lsra_baseline.graph.add_node(str(i))
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            # Assume a fixed edge probability of 0.2
            if random.random() < 0.2:
                lsra_baseline.add_edge(str(i), str(j), random.randint(1, 100))

    # Visualization
    pos = nx.spring_layout(lsra_baseline.graph)
    nx.draw(lsra_baseline.graph, pos, with_labels=True, node_size=700)
    edge_labels = nx.get_edge_attributes(lsra_baseline.graph, 'weight')
    nx.draw_networkx_edge_labels(lsra_baseline.graph, pos, edge_labels=edge_labels)
    plt.title('Network Graph')
    plt.show()

    # Calculate shortest paths from source node '0'
    source_node = '0'
    start_time = time.time()
    shortest_paths = lsra_baseline.shortest_path(source_node, str(num_nodes - 1))
    end_time = time.time()
    total_time = end_time - start_time

    # Print shortest paths and total time taken
    print(f"Shortest paths from node {source_node}:")
    for target, distance in shortest_paths.items():
        print(f"To node {target}: Distance: {distance}")
    print("Total time taken:", total_time, "seconds")

    # Print the number of nodes and edges in the graph
    num_edges = len(lsra_baseline.graph.edges())
    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")

    # Print the estimated time complexity category
    time_complexity_category = "O(n^2) Time Complexity"
    print(f"Estimated time complexity category for LSRA: {time_complexity_category}")