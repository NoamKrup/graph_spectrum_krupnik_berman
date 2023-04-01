import sys
import os
import networkx as nx
import matplotlib.pyplot as plt
import scipy
from scipy import linalg

def crete_simple_graph():
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2, 3])
    G.add_edge(1, 2)
    e = (2, 3)
    G.add_edge(*e)
    # G.add_edges_from([(3, 4), (4, 5), (1, 5)])
    # G.add_edges_from([(1, 2, {"color": "blue"}), (2, 3, {"weight": 8})])
    return G


def get_eigenvalues_of_graph(G):
    A = nx.adjacency_matrix(G)
    print(f'Adjacency matrix :\n{A.todense()}'.replace("[", "").replace("]", "").replace("\n ", "\n"))
    eigenvalues = linalg.eigh(A.todense(),  eigvals_only=True)
    #round eigenvalues to 4 decimal places
    eigenvalues = [round(eigenvalue, 4) for eigenvalue in eigenvalues]
    return eigenvalues

if __name__ == '__main__':
    eigenvalues_set = set()
    G = crete_simple_graph()
    nx.draw(G, with_labels=True)
    A = nx.adjacency_matrix(G)
    eigenvalues = get_eigenvalues_of_graph(G)
    eigenvalues_set.add(tuple(eigenvalues))
    print(f'Eigenvalues of graph G: {eigenvalues}')
    print(f'Eigenvalues set: {eigenvalues_set}')
    # plt.show()
