import networkx as nx
from scipy import linalg
import itertools
import arithmetic_utils as au
import numpy as np
import matrix_utils as mu
import random

def get_adjacency_matrix(G):
    A = nx.adjacency_matrix(G)
    return A.todense()


def get_formatted_adjacency_matrix(g):
    a = get_adjacency_matrix(g)
    return f'{a}'.replace("[", "").replace("]", "").replace("\n ", "\n")


def get_n_from_graphs_set(graphs):
    for g in graphs:
        return len(g.nodes())



def get_eigenvalues_of_graph(g):
    a = nx.adjacency_matrix(g).todense()
    eigenvalues = mu.get_eigenvalues_of_a_matrix(a)
    return eigenvalues


def reduce_graphs(graphs):
    adj_matrices = list()
    # create adjacency matrices
    for g in graphs:
        a = nx.adjacency_matrix(g).toarray()
        adj_matrices.append(a)
        # a = get_adjacency_matrix(g)
    # remove permutations
    initial_list_length = len(adj_matrices)
    permutation_mateices = mu.generate_all_permutation_matrices(get_n_from_graphs_set(graphs))
    for main_matrix in adj_matrices:
        for p in permutation_mateices:
            p_times_matrix = np.matmul(p, main_matrix)
            permuted_matrix = np.matmul(p_times_matrix, p.transpose())
            for secondary_matrix in adj_matrices:
                if mu.is_matrices_equal(secondary_matrix, permuted_matrix) and not mu.is_matrices_equal(main_matrix, secondary_matrix):
                    mu.remove_matrix_from_list(adj_matrices, permuted_matrix)
                    print(f'original matrix \n{main_matrix}, removed_matrix \n{permuted_matrix}')
    final_list_length = len(adj_matrices)
    print(f'started with : {initial_list_length} possible graphs \nended with {final_list_length} graphs that are not isomorphic to each other')
    return adj_matrices


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
