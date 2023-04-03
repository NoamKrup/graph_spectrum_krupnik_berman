import networkx as nx
from scipy import linalg
from itertools import chain, combinations


def create_simple_graph_with_edges(edges):
    g = nx.Graph()
    g.add_nodes_from([1, 2, 3, 4])
    g.add_edges_from(edges)
    return g


def get_adjacency_matrix(G):
    A = nx.adjacency_matrix(G)
    return A.todense()


def get_formatted_adjacency_matrix(G):
    A = get_adjacency_matrix(G)
    return f'{A}'.replace("[", "").replace("]", "").replace("\n ", "\n")


def get_eigenvalues_of_graph(G):
    A = nx.adjacency_matrix(G)
    print(f'Adjacency matrix :\n{A.todense()}'.replace("[", "").replace("]", "").replace("\n ", "\n"))
    eigenvalues = linalg.eigh(A.todense(), eigvals_only=True)
    # round eigenvalues to 4 decimal places
    eigenvalues = [round(eigenvalue, 4) for eigenvalue in eigenvalues]
    return eigenvalues
