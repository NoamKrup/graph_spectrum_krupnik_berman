import sys
import os
import networkx as nx
import matplotlib.pyplot as plt
import scipy
from scipy import linalg
from itertools import chain, combinations
import graph_utils as gu
import arithmetic_utils as au
import sandbox

def create_all_graphes_with_n_vertices(n):
    if n == 1:
        g = nx.Graph()
        g.add_node(1)
        return [g]
    else:
        graphs = set()
        smaller_sub_graphs = create_all_graphes_with_n_vertices(n - 1)
        for g in smaller_sub_graphs:
            g0 = g.copy()
            g0.add_node(n)
            subgraph_vertices = list(range(1, n))
            for vertices in au.powerset(subgraph_vertices):
                g1 = g0.copy()
                for vertex in vertices:
                    g1.add_edge(n, vertex)
                    # adj = nx.adjacency_matrix(g1)
                    # print(adj.todense(), "\n")
                    graphs.add(g1)
        return graphs


if __name__ == '__main__':
    eigenvalues_set = set()
    a_matrix_set = set()
    graphs = create_all_graphes_with_n_vertices(4)
    for g in graphs:
        formated_adjacency_matrix = gu.get_formatted_adjacency_matrix(g);
        print(f'Adjacency matrix of graph G:\n{formated_adjacency_matrix}\n')
        # a_matrix_set.add(gu.get_adjacency_matrix(g))

