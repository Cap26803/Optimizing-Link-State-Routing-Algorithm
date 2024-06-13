# @author: Chinmay Paranjape, Kushal Kaparatti, Prathamesh Chitnis
# @version: v1.2.0
# @date: 13-JUN-2024

import base64
import io
import os
import random
import time

import matplotlib.pyplot as plt
import networkx as nx
from flask import Flask, render_template, request

from lsra_baseline import LSRA_Baseline
from lsra_optimized import (LSRA_Hierarchical, connect_clusters,
                            ensure_dense_connectivity,
                            generate_connected_graph)

app = Flask(__name__)


def plot_graph(graph):
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(10, 7))
    nx.draw(graph, pos, with_labels=True, node_size=700)
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode("utf8")
    plt.close()
    return plot_url


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        num_nodes = int(request.form["num_nodes"])

        # Baseline Algorithm
        lsra_baseline = LSRA_Baseline()
        for i in range(num_nodes):
            lsra_baseline.graph.add_node(str(i))
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if random.random() < 0.2:
                    lsra_baseline.add_edge(str(i), str(j), random.randint(1, 100))
        baseline_plot = plot_graph(lsra_baseline.graph)
        baseline_time_start = time.time()
        baseline_shortest_paths = lsra_baseline.shortest_path("0", str(num_nodes - 1))
        baseline_time_end = time.time()
        baseline_time = baseline_time_end - baseline_time_start

        # Optimized Algorithm
        graph, graph_gen_time = generate_connected_graph(num_nodes, 0.25)
        graph, dense_connectivity_time = ensure_dense_connectivity(
            graph, num_nodes, 0.25
        )
        lsra_optimized = LSRA_Hierarchical(graph)
        cluster_connection_time = connect_clusters(graph, lsra_optimized.clusters, 0.25)
        optimized_plot = plot_graph(graph)
        optimized_time_start = time.time()
        optimized_shortest_paths = lsra_optimized.shortest_paths_from_source("0")
        optimized_time_end = time.time()
        optimized_time = optimized_time_end - optimized_time_start

        return render_template(
            "index.html",
            num_nodes=num_nodes,
            baseline_plot=baseline_plot,
            baseline_shortest_paths=baseline_shortest_paths,
            baseline_time=baseline_time,
            optimized_plot=optimized_plot,
            optimized_shortest_paths=optimized_shortest_paths,
            optimized_time=optimized_time,
        )
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
