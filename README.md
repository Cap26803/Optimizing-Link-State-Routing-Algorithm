# Optimizing Link State Routing Algorithm

## Problem Statement
This project aims to optimize the Link State Routing Algorithm (LSRA) using NetworkX, a Python library for graph analysis. The project focuses on enhancing the efficiency of shortest path calculations, reducing routing convergence time, and simplifying LSRA implementation for network simulations.

## Objectives
1. Enhance the efficiency of shortest path calculations.
2. Reduce routing convergence time.
3. Simplify LSRA implementation for network simulations.

## Implementation Details

### Programming Language

- Python 3.8

### Libraries

- *NetworkX*: Used for network representation and pathfinding functionalities.
- *Matplotlib*: For plotting graphs and visualizing the results.

### Class Diagram

- LSRAHierarchical: Implements various optimization techniques for improving LSRA efficiency.
- Graph: Represents the network graph and provides methods for graph manipulation.

### Sequence Diagram

1. User creates a graph with nodes and edges.
2. The LSRAHierarchical module adds nodes and edges to the Graph.
3. Clusters are formed within the Graph.
4. Gateway nodes are assigned to the clusters.
5. Paths are precomputed within each cluster.
6. User requests the shortest path from a source node to a destination node.
7. The shortest path is computed and returned to the user.

### Activity Diagram

1. Create a graph.
2. Generate a connected graph with nodes and edges.
3. Form clusters.
4. Assign gateway nodes.
5. Precompute paths.
6. Check if source and target are in the same cluster.
7. Combine intra-cluster and inter-cluster paths if necessary.
8. Return shortest paths.

### Context Diagram

- The system consists of a user interacting with the LSRA-Hierarchical module.
- The LSRA-Hierarchical module utilizes the Graph component to represent the network topology with nodes and edges.
- The interactions involve creating, manipulating, and analyzing graphs to compute shortest paths and optimize network routing.

## Results and Outcomes

- The optimized algorithm reduces the computational overhead associated with maintaining and utilizing the network map in large-scale simulations.
- It also improves the adaptability of routers within the simulation to network changes, ensuring efficient routing convergence.

## Conclusion

The project successfully optimizes the Link-State Routing Algorithm for network simulation environments, providing a more efficient and adaptable tool for developers and researchers.

## Contributors

- Kushal Kaparatti 
- Prathamesh Chitnis 
- Chinmay Paranjape
