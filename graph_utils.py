import networkx as nx
from scipy import linalg
import itertools
import arithmetic_utils as au
import numpy as np
import matrix_utils as mu
from enum import Enum


class GraphFormat(Enum):
    MATRIX = 1
    NXGRAPH = 2


def format_graph(graph, format):
    if format == GraphFormat.MATRIX:
        if isinstance(graph, nx.classes.graph.Graph):
            return nx.adjacency_matrix(graph).toarray()
        else:
            return graph
    elif format == GraphFormat.NXGRAPH:
        if isinstance(graph, nx.classes.graph.Graph):
            return graph
        else:
            return nx.from_numpy_array(graph)


def format_graph_list(graphs, format):
    output = list()
    for g in graphs:
        output.append(format_graph(g, format))
    return output


def new_reduce_graphs(graphs, input_format=GraphFormat.MATRIX, output_format=GraphFormat.MATRIX):
    output = list()
    if input_format == GraphFormat.NXGRAPH:
        graphs = [format_graph(g, GraphFormat.MATRIX) for g in graphs]
    if len(graphs) == 1:
        output = [graphs[0]]

    # massage output
    if output_format == GraphFormat.NXGRAPH:
        output = [nx.from_numpy_array(m) for m in output]


def reduce_graphs(graphs, input_format=GraphFormat.MATRIX, output_format=GraphFormat.MATRIX):
    if len(graphs) == 1:
        return [nx.adjacency_matrix(graphs[0]).toarray()]
    adj_matrices = list()
    # create adjacency matrices
    for g in graphs:
        a = nx.adjacency_matrix(g).toarray()
        adj_matrices.append(a)
    # remove permutations
    initial_list_length = len(adj_matrices)
    permutation_mateices = mu.generate_all_permutation_matrices(get_n_from_graphs_set(graphs))
    for main_matrix in adj_matrices:
        for p in permutation_mateices:
            p_times_matrix = np.matmul(p, main_matrix)
            permuted_matrix = np.matmul(p_times_matrix, p.transpose())
            if not mu.is_matrices_equal(main_matrix, permuted_matrix):
                for secondary_matrix in adj_matrices:
                    if mu.is_matrices_equal(secondary_matrix, permuted_matrix):
                        mu.remove_matrix_from_list(adj_matrices, permuted_matrix)
    final_list_length = len(adj_matrices)
    return adj_matrices


def create_Iso_quotient_set_of_n_vertices(n):
    if n == 1:
        g = nx.Graph()
        g.add_node(1)
        return [format_graph(g, s.GraphFormat.MATRIX)]
    else:
        graphs_with_n_vertices = set()
        graphs = create_Iso_quotient_set_of_n_vertices(n - 1)



def create_all_graphes_with_n_vertices_as_matrices(n):
    if n == 1:
        g = nx.Graph()
        g.add_node(1)
        return [g]
    else:
        graphs = set()
        smaller_sub_graphs = create_all_graphes_with_n_vertices_as_matrices(n - 1)
        reduced_subgraphs_matrices = reduce_graphs(smaller_sub_graphs, output_format=GraphFormat.NXGRAPH)
        for m in reduced_subgraphs_matrices:
            g = nx.from_numpy_array(m)
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


def create_all_graphes_with_n_vertices(n):
    if n == 1:
        g = nx.Graph()
        g.add_node(1)
        return [g]
    else:
        graphs = set()
        smaller_sub_graphs = create_all_graphes_with_n_vertices(n - 1)
        reduced_subgraphs = reduce_graphs(smaller_sub_graphs, output_format=GraphFormat.NXGRAPH)
        for g in reduced_subgraphs:
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
