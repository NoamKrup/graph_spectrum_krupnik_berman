import networkx as nx
from scipy import linalg
import itertools
import arithmetic_utils as au
import numpy as np


def get_adjacency_matrix(G):
    A = nx.adjacency_matrix(G)
    return A.todense()


def get_formatted_adjacency_matrix(g):
    a = get_adjacency_matrix(g)
    return f'{a}'.replace("[", "").replace("]", "").replace("\n ", "\n")

def format_matrix_for_printing(g, name):
    adjacency_matrix = get_adjacency_matrix(g)
    formated_adjacency_matrix = f'{adjacency_matrix}'.replace("[", "").replace("]", "").replace("\n ", "\n")
    eigenvalues = get_eigenvalues_of_graph(g)
    formated_eigenvalues = format_eigenvalues(eigenvalues)
    text = f'------ graph {name} -----------\n'
    text += f'Adjacency matrix :\n{formated_adjacency_matrix}\n'
    text += f'Eigenvalues : {formated_eigenvalues}\n\n'
    return text


def format_eigenvalues(eigenvalues):
    eigenvalues = [round(eigenvalue, 4) for eigenvalue in eigenvalues]
    eigenvalues2 = list(map(lambda x: 0 if x == 0 or x == -0 else x, eigenvalues))
    return eigenvalues2

def get_eigenvalues_of_graph(G):
    A = nx.adjacency_matrix(G)
    eigenvalues = linalg.eigh(A.todense(), eigvals_only=True)
    # round eigenvalues to 4 decimal places
    eigenvalues = format_eigenvalues(eigenvalues)
    return eigenvalues


def reduce_graphs(graphs):
    adj_matrices = list()
    for g in graphs:
        a = get_adjacency_matrix(g)
        adj_matrices.append(a)
    # for mat in adj_matrices:
        # permutation = generate_all_permutations(len(mat))
        # permutation_matrices = [p * mat * p.transpose() for p in permutation]
        # for m in itertools.permutations(permutation):
        #
        #     perm_mat = perm.todense()
        #     perm_graph = perm_mat * mat * perm_mat.transpose()
        #     if perm_mat in adj_matrices and perm_mat != mat:
        #         graphs.remove(g)


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
