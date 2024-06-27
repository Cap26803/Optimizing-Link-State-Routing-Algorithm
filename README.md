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

## Design
### Class Diagram
![LSRA_ClassDiagram](https://github.com/Cap26803/Optimizing-Link-State-Routing-Algorithm/assets/106472393/780b07c7-eefe-4f86-927f-bf85047c3d80)

### Sequence Diagram
![LSRA_SequenceDiagram](https://github.com/Cap26803/Optimizing-Link-State-Routing-Algorithm/assets/106472393/35776228-fa02-4495-8b99-8f436baa9e23)

1. User creates a graph with nodes and edges.
2. The LSRAHierarchical module adds nodes and edges to the Graph.
3. Clusters are formed within the Graph.
4. Gateway nodes are assigned to the clusters.
5. Paths are precomputed within each cluster.
6. User requests the shortest path from a source node to a destination node.
7. The shortest path is computed and returned to the user.

### Activity Diagram
![LSRA_ActivityDiagram](https://github.com/Cap26803/Optimizing-Link-State-Routing-Algorithm/assets/106472393/667f6c3a-68cc-48e5-8257-dd54d18c4210)

1. Create a graph.
2. Generate a connected graph with nodes and edges.
3. Form clusters.
4. Assign gateway nodes.
5. Precompute paths.
6. Check if source and target are in the same cluster.
7. Combine intra-cluster and inter-cluster paths if necessary.
8. Return shortest paths.

### Context Diagram
![LSRA_ContextDiagram](https://github.com/Cap26803/Optimizing-Link-State-Routing-Algorithm/assets/106472393/86bc0795-b614-468d-8e4f-b178fe644852)

- The system consists of a user interacting with the LSRA-Hierarchical module.
- The LSRA-Hierarchical module utilizes the Graph component to represent the network topology with nodes and edges.
- The interactions involve creating, manipulating, and analyzing graphs to compute shortest paths and optimize network routing.

## Results and Outcomes

- The optimized algorithm reduces the computational overhead associated with maintaining and utilizing the network map in large-scale simulations.
- It also improves the adaptability of routers within the simulation to network changes, ensuring efficient routing convergence.

### Generated Graphs

#### Baseline Graph
![1000 BA](https://github.com/Cap26803/Optimizing-Link-State-Routing-Algorithm/assets/106472393/e94f6781-3ba2-4317-8b2a-eb2d1a068f0d)
#### Optimized Graph
![1000 OA](https://github.com/Cap26803/Optimizing-Link-State-Routing-Algorithm/assets/106472393/ccb5562c-39b0-465a-b3f4-00af09e199c1)

### Comparision Results

#### Comparision of Baseline and Optimized Algorithm Times
![compare_time](https://github.com/Cap26803/Optimizing-Link-State-Routing-Algorithm/assets/106472393/cb8675fc-d515-4225-90c2-789a7470281f)

#### Cluster Count Linear Graph for Optimized Algorithm
![compare_cluster](https://github.com/Cap26803/Optimizing-Link-State-Routing-Algorithm/assets/106472393/491a3a27-89e1-4b14-b979-8964113c2c3d)
 
## Conclusion

This project successfully addressed the challenge of improving the computational efficiency of the Link-State Routing Algorithm (LSRA) within network simulations. As network simulations become larger and more complex, traditional LSRA implementations can become a bottleneck, hindering simulation speed and scalability.

## Contributors
- Chinmay Paranjape
- Kushal Kaparatti 
- Prathamesh Chitnis 

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
