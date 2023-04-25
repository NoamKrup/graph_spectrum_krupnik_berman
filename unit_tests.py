import numpy as np
import itertools
import networkx as nx
import graph_utils as gu
import arithmetic_utils as au
import matrix_utils as mu
from scipy import linalg
from collections import Counter


def test_spectrum_classification_without_permutated_repetitions(n):
    eigenvalues_counter = Counter()
    graphs = gu.create_all_graphes_with_n_vertices(n)
    matrices = gu.reduce_graphs(graphs, )
    matrices_counter = 1
    for m in matrices:
        eigenvalues = mu.get_eigenvalues_of_a_matrix(m)
        eigenvalues_tuple = tuple(eigenvalues)
        eigenvalues_counter.update(eigenvalues_tuple)
        matrices_counter += 1
    return eigenvalues_counter


def test_create_all_graphes_with_n_vertices_and_print_to_file(n):
    graphs = gu.create_all_graphes_with_n_vertices(n)
    text = ''
    graph_counter = 1
    file_name = f'outputs/graphs_{n}_vertices.txt'
    for g in graphs:
        text += gu.format_graph_for_printing(g, graph_counter)
        graph_counter += 1
    au.print_to_file(file_name, text)


def test_permutations_01(n):
    permutation_matrices = mu.generate_all_permutation_matrices(n)
    counter = 1
    for p in permutation_matrices:
        print(f'permutation matrix {counter}')
        print(p)
        print()
        counter += 1