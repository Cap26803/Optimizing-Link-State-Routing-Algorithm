import networkx as nx


class LSRA:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, node1, node2, weight):
        self.graph.add_edge(node1, node2, weight=weight)

    def shortest_path(self, source, target):
        return nx.shortest_path(self.graph, source=source, target=target, weight='weight')

if __name__ == "__main__":
    lsra = LSRA()
    lsra.add_edge('A', 'B', 1)
    lsra.add_edge('A', 'C', 2)
    lsra.add_edge('B', 'C', 1)
    lsra.add_edge('B', 'D', 3)
    lsra.add_edge('C', 'D', 1)
    print("Shortest path from A to D:", lsra.shortest_path('A', 'D'))