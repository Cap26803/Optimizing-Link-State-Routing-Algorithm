import random
import time

import matplotlib.pyplot as plt
import networkx as nx


class LSRA:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, node1, node2, weight):
        self.graph.add_edge(node1, node2, weight=weight)

    def shortest_path(self, source, target):
        return nx.shortest_path(self.graph, source=source, target=target, weight='weight')

    def shortest_paths_from_source(self, source):
        shortest_paths = {}
        for target in self.graph.nodes():
            if target != source:
                shortest_paths[target] = self.shortest_path(source, target)
        return shortest_paths

if __name__ == "__main__":
    lsra = LSRA()
    
    # Add 50 nodes with random edges and weights
    for i in range(50):
        lsra.graph.add_node(str(i))
    for i in range(50):
        for j in range(i+1, 50):
            if random.random() < 0.2:  # Probability of having an edge between nodes
                lsra.add_edge(str(i), str(j), random.randint(1, 100))

    # Visualization
    pos = nx.spring_layout(lsra.graph)  
    nx.draw(lsra.graph, pos, with_labels=True, node_size=700)  
    edge_labels = nx.get_edge_attributes(lsra.graph, 'weight')  
    nx.draw_networkx_edge_labels(lsra.graph, pos, edge_labels=edge_labels)  
    plt.title('Network Graph')
    plt.show()
    
    # Calculate shortest paths from source node '0'
    source_node = '0'
    start_time = time.time()
    shortest_paths = lsra.shortest_paths_from_source(source_node)
    end_time = time.time()
    total_time = end_time - start_time

    # Print shortest paths and total time taken
    print(f"Shortest paths from node {source_node}:")
    for target, path in shortest_paths.items():
        distance = sum(lsra.graph[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))
        print(f"To node {target}: Path: {path}, Distance: {distance}")
    print("Total time taken:", total_time, "seconds")

    # Calculate the number of nodes and edges in the graph
    num_nodes = len(lsra.graph.nodes())
    num_edges = len(lsra.graph.edges())

    # Print the estimated time complexity category
    time_complexity_category = "O(n log n) Time Complexity"
    print(f"Estimated time complexity category for LSRA: {time_complexity_category}")
