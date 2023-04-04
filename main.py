import sys
import os
import networkx as nx
import matplotlib.pyplot as plt
import scipy
from scipy import linalg
from itertools import chain, combinations
from collections import Counter

# my stuff
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
            graphs.add(g0)
            for vertices in au.powerset(subgraph_vertices):
                g1 = g0.copy()
                for vertex in vertices:
                    g1.add_edge(n, vertex)
                    graphs.add(g1)
        return graphs


def get_eigenvalues_multy_set(graphs):
    eigenvalues_set = set()
    graphs = create_all_graphes_with_n_vertices(5)
    for g in graphs:
        eigenvalues = gu.get_eigenvalues_of_graph(g)
        eigenvalues_set.add(tuple(eigenvalues))
    return eigenvalues_set


def print_all_graphs_with_n_vertices_to_file(n):
    graphs = create_all_graphes_with_n_vertices(n)
    text = ''
    graph_counter = 1
    file_name = f'graphs_{n}_vertices.txt'
    for g in graphs:
        formated_adjacency_matrix = gu.get_formatted_adjacency_matrix(g)
        eigenvalues = gu.get_eigenvalues_of_graph(g)
        formated_eigenvalues = gu.format_eigenvalues(eigenvalues)
        text += f'------ graph {graph_counter} -----------\n'
        text += f'Adjacency matrix :\n{formated_adjacency_matrix}\n'
        text += f'Eigenvalues : {formated_eigenvalues}\n\n'
        graph_counter += 1
    au.print_to_file(file_name, text)


if __name__ == '__main__':
    print_all_graphs_with_n_vertices_to_file(4)

    # for g in graphs:
    #     formated_adjacency_matrix = gu.get_formatted_adjacency_matrix(g)
    #     print(f'Adjacency matrix of the {graph_counter}\'s graph:\n{formated_adjacency_matrix}\n')
    #     eigenvalues = gu.get_eigenvalues_of_graph(g)
    #     formated_eigenvalues = gu.format_eigenvalues(eigenvalues)
    #     print(f'Eigenvalues of the {graph_counter}\'s graph: {formated_eigenvalues}\n')
    #     graph_counter += 1
        # a_matrix_set.add(gu.get_adjacency_matrix(g))

