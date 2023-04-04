import networkx as nx
from scipy import linalg
from itertools import chain, combinations
import arithmetic_utils as au

def create_simple_graph_with_edges(edges):
    g = nx.Graph()
    g.add_nodes_from([1, 2, 3, 4])
    g.add_edges_from(edges)
    return g


def get_adjacency_matrix(G):
    A = nx.adjacency_matrix(G)
    return A.todense()


def get_formatted_adjacency_matrix(g):
    a = get_adjacency_matrix(g)
    return f'{a}'.replace("[", "").replace("]", "").replace("\n ", "\n")


def format_eigenvalues(eigenvalues):
    eigenvalues = [round(eigenvalue, 4) for eigenvalue in eigenvalues]
    eigenvalues2 = list(map(lambda x: 0 if x == 0 or x == -0 else x, eigenvalues))
    return eigenvalues2

def get_eigenvalues_of_graph(G):
    A = nx.adjacency_matrix(G)
    printable = f'Adjacency matrix :\n{A.todense()}'.replace("[", "").replace("]", "").replace("\n ", "\n")
    eigenvalues = linalg.eigh(A.todense(), eigvals_only=True)
    # round eigenvalues to 4 decimal places
    eigenvalues = format_eigenvalues(eigenvalues)
    return eigenvalues


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
