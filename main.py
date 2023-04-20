import sys
import os
import networkx as nx
import matplotlib.pyplot as plt
import scipy
from scipy import linalg
from itertools import chain, combinations
from collections import Counter
import unit_tests

# my stuff
import graph_utils as gu
import matrix_utils as mu
import arithmetic_utils as au
import printing_utils as pu
import sandbox



# MAIN
def print_n_vertices_graphs_relevant_file(n):
    graphs = gu.create_all_graphes_with_n_vertices(n)
    pu.print_all_graphs_to_file(graphs)
    reduced_graph_matrices_set = pu.get_reduced_graphs_and_print_to_file(graphs)
    pu.print_eigenvalues_counter_to_file(reduced_graph_matrices_set)

def print_n_vertices_eigen_only_to_relevant_file(n):
    graphs = gu.create_all_graphes_with_n_vertices(n)
    reduced_graph_matrices_set = pu.get_reduced_graphs_and_print_to_file(graphs)
    pu.print_eigenvalues_counter_to_file(reduced_graph_matrices_set)


if __name__ == '__main__':
    n = 4
    print_n_vertices_eigen_only_to_relevant_file(n)
    # sandbox.crete_simple_graph()


    # n = 5
    # print_all_graphs_with_n_vertices_to_file(n)
    # eigenvalues = get_n_vertices_eigenvalues_multy_set(n)
    # au.print_eigenvalues_counter_to_file(eigenvalues, n)
    # graphs = create_all_graphes_with_n_vertices(4)
    # print_all_graphs_with_n_vertices_to_file(4)

