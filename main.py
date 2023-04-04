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


def print_all_graphs_with_n_vertices_to_file(n):
    graphs = gu.create_all_graphes_with_n_vertices(n)
    text = ''
    graph_counter = 1
    file_name = f'outputs/graphs_{n}_vertices.txt'
    for g in graphs:
        formated_adjacency_matrix = gu.get_formatted_adjacency_matrix(g)
        eigenvalues = gu.get_eigenvalues_of_graph(g)
        formated_eigenvalues = gu.format_eigenvalues(eigenvalues)
        text += f'------ graph {graph_counter} -----------\n'
        text += f'Adjacency matrix :\n{formated_adjacency_matrix}\n'
        text += f'Eigenvalues : {formated_eigenvalues}\n\n'
        graph_counter += 1
    au.print_to_file(file_name, text)


def get_n_vertices_eigenvalues_multy_set(n):
    eigenvalues_counter = Counter()
    graphs = gu.create_all_graphes_with_n_vertices(n)
    graphs_counter = 1
    for g in graphs:
        eigenvalues = gu.get_eigenvalues_of_graph(g)
        eigenvalues_tuple = [tuple(eigenvalues)]
        eigenvalues_counter.update(eigenvalues_tuple)
        graphs_counter += 1
    return eigenvalues_counter


if __name__ == '__main__':
    n = 5
    print_all_graphs_with_n_vertices_to_file(n)
    eigenvalues = get_n_vertices_eigenvalues_multy_set(n)
    au.print_eigenvalues_counter_to_file(eigenvalues, n)
    # graphs = create_all_graphes_with_n_vertices(4)
    # print_all_graphs_with_n_vertices_to_file(4)
