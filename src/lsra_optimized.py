# @author: Chinmay Paranjape, Kushal Kaparatti, Prathamesh Chitnis
# @version: v1.2.0
# @date: 13-JUN-2024

import random
import time

import matplotlib.pyplot as plt
import networkx as nx


class LSRA_Hierarchical:
    def __init__(self, graph):
        self.graph = graph
        self.clusters = []
        self.gateway_nodes = {}
        self.precomputed_paths = {}
        self.form_clusters()
        self.assign_gateway_nodes()
        self.precompute_paths()

    def add_edge(self, node1, node2, weight):
        self.graph.add_edge(node1, node2, weight=weight)

    def form_clusters(self):
        start_time = time.time()
        num_clusters = 5  # Number of clusters
        nodes = list(self.graph.nodes())
        random.shuffle(nodes)
        cluster_size = len(nodes) // num_clusters
        for i in range(num_clusters):
            self.clusters.append(nodes[i * cluster_size:(i + 1) * cluster_size])
        if len(nodes) % num_clusters != 0:
            self.clusters[-1].extend(nodes[num_clusters * cluster_size:])
        end_time = time.time()
        self.clustering_time = end_time - start_time

    def assign_gateway_nodes(self):
        start_time = time.time()
        for cluster in self.clusters:
            gateway_node = cluster[0]  # Assign the first node in the cluster as the gateway
            self.gateway_nodes[gateway_node] = cluster
        end_time = time.time()
        self.gateway_assignment_time = end_time - start_time

    def precompute_paths(self):
        start_time = time.time()
        for node in self.graph.nodes():
            self.precomputed_paths[node] = nx.single_source_dijkstra_path(self.graph, source=node, weight='weight')
        end_time = time.time()
        self.precomputation_time = end_time - start_time

    def intra_cluster_shortest_path(self, source, target):
        cluster = self.find_cluster(source)
        subgraph = self.graph.subgraph(cluster)
        return nx.shortest_path(subgraph, source=source, target=target, weight='weight')

    def inter_cluster_shortest_path(self, source, target):
        source_gateway = self.find_gateway(source)
        target_gateway = self.find_gateway(target)

        path1 = self.intra_cluster_shortest_path(source, source_gateway)
        path2 = nx.shortest_path(self.graph, source=source_gateway, target=target_gateway, weight='weight')
        path3 = self.intra_cluster_shortest_path(target_gateway, target)

        full_path = path1 + path2[1:] + path3[1:]
        return full_path

    def shortest_path(self, source, target):
        if source == target:
            return [source]
        source_cluster = self.find_cluster(source)
        target_cluster = self.find_cluster(target)

        if source_cluster == target_cluster:
            return self.intra_cluster_shortest_path(source, target)
        else:
            return self.inter_cluster_shortest_path(source, target)

    def shortest_paths_from_source(self, source):
        start_time = time.time()
        shortest_paths = {}
        for target in self.graph.nodes():
            if target != source:
                try:
                    shortest_paths[target] = self.shortest_path(source, target)
                except nx.NetworkXNoPath:
                    shortest_paths[target] = None
        end_time = time.time()
        self.shortest_path_calculation_time = end_time - start_time
        return shortest_paths

    def find_cluster(self, node):
        for cluster in self.clusters:
            if node in cluster:
                return cluster
        return None

    def find_gateway(self, node):
        cluster = self.find_cluster(node)
        for gateway, cluster_nodes in self.gateway_nodes.items():
            if set(cluster) == set(cluster_nodes):
                return gateway
        return None

def generate_connected_graph(num_nodes, edge_probability):
    start_time = time.time()
    graph = nx.Graph()
    for i in range(num_nodes):
        graph.add_node(str(i))
    while not nx.is_connected(graph):
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if random.random() < edge_probability:
                    graph.add_edge(str(i), str(j), weight=random.randint(1, 100))
    end_time = time.time()
    graph_generation_time = end_time - start_time
    return graph, graph_generation_time

def ensure_dense_connectivity(graph, num_nodes, edge_probability):
    start_time = time.time()
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if not graph.has_edge(str(i), str(j)):
                if random.random() < edge_probability:
                    graph.add_edge(str(i), str(j), weight=random.randint(1, 100))
    end_time = time.time()
    dense_connectivity_time = end_time - start_time
    return graph, dense_connectivity_time

def connect_clusters(graph, clusters, edge_probability):
    start_time = time.time()
    for cluster in clusters:
        for other_cluster in clusters:
            if cluster != other_cluster:
                for node1 in cluster:
                    for node2 in other_cluster:
                        if random.random() < edge_probability and not graph.has_edge(node1, node2):
                            graph.add_edge(node1, node2, weight=random.randint(1, 100))
    end_time = time.time()
    cluster_connection_time = end_time - start_time
    return cluster_connection_time

def calculate_time_complexity(num_nodes, num_edges, graph_gen_time, cluster_time, gateway_time, precomp_time, shortest_path_time):
    graph_generation = f"O(n^2 * p) where p is edge probability"
    clustering = f"O(n)"
    gateway_assignment = f"O(k) where k is the number of clusters"
    precomputation = f"O(n * (n log n + e)) where e = {num_edges}"
    shortest_path_calc = f"O(n log n + e) where e = {num_edges}"
    overall_time_complexity = f"O(n * (n log n + e))"

    return {
        "Graph Generation": (graph_generation, graph_gen_time),
        "Clustering": (clustering, cluster_time),
        "Gateway Assignment": (gateway_assignment, gateway_time),
        "Precomputation": (precomputation, precomp_time),
        "Shortest Path Calculation": (shortest_path_calc, shortest_path_time),
        "Overall Time Complexity": overall_time_complexity
    }

if __name__ == "__main__":
    num_nodes = int(input("Enter the number of nodes: "))  # Prompt user to input the number of nodes
    edge_probability = 0.25

    graph, graph_gen_time = generate_connected_graph(num_nodes, edge_probability)
    graph, dense_connectivity_time = ensure_dense_connectivity(graph, num_nodes, edge_probability)

    lsra_hierarchical = LSRA_Hierarchical(graph)
    cluster_connection_time = connect_clusters(graph, lsra_hierarchical.clusters, edge_probability)

    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=700)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title('Network Graph')
    plt.show(block=True)  # Display the graph and keep the window open

    source_node = '0'
    shortest_paths = lsra_hierarchical.shortest_paths_from_source(source_node)

    print(f"Shortest paths from node {source_node}:")
    for target, path in shortest_paths.items():
        if path:
            distance = sum(lsra_hierarchical.graph[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))
            print(f"To node {target}: Path: {path}, Distance: {distance}")
        else:
            print(f"To node {target}: No path found")
    print("Total shortest path calculation time:", lsra_hierarchical.shortest_path_calculation_time, "seconds \n")

    num_nodes = len(graph.nodes())
    num_edges = len(graph.edges())

    time_complexity_info = calculate_time_complexity(
        num_nodes, num_edges, graph_gen_time, lsra_hierarchical.clustering_time,
        lsra_hierarchical.gateway_assignment_time, lsra_hierarchical.precomputation_time,
        lsra_hierarchical.shortest_path_calculation_time
    )

    for step, value in time_complexity_info.items():
        if step == "Overall Time Complexity":
            print(f"{step} - {value}")
        else:
            complexity, duration = value
            print(f"{step} - Complexity: {complexity}, Time: {duration:.6f} seconds")
