import graph_utils as gu
import matplotlib.pyplot as plt
import networkx as nx
import matrix_utils as mu
import arithmetic_utils as au
import numpy as np

def first_sandgame():
    eigenvalues_set = set()
    G1 = crete_simple_graph()
    e = (1, 3)
    G2 = gu.create_simple_graph_with_edges([e])
    # nx.draw(G1, with_labels=True)
    nx.draw(G2, with_labels=True)
    A = nx.adjacency_matrix(G1)
    eigenvalues = gu.get_eigenvalues_of_graph(G1)
    eigenvalues_set.add(tuple(eigenvalues))
    print(f'Eigenvalues of graph G: {eigenvalues}')
    print(f'Eigenvalues set: {eigenvalues_set}')
    plt.show()


def crete_simple_graph():
    g = nx.Graph()
    g.add_node(1)
    g.add_nodes_from([2, 3])
    g.add_edge(1, 2)
    e = (2, 3)
    g.add_edge(*e)
    # G.add_edges_from([(3, 4), (4, 5), (1, 5)])
    # G.add_edges_from([(1, 2, {"color": "blue"}), (2, 3, {"weight": 8})])
    return g


def reduce_graphs(graphs):
    adj_matrices = list()
    # create adjacency matrices
    for g in graphs:
        a = nx.adjacency_matrix(g)
        adj_matrices.update(a)
        # a = get_adjacency_matrix(g)
    # remove permutations
    permutation_mateices = mu.generate_all_permutation_matrices(len(adj_matrices[0]))
    for matrix in adj_matrices:
        for p in permutation_mateices:
            permuted_matrix = np.matmul(np.matmul(p, matrix), p.transpose()).tolist()
            t = type(permuted_matrix) #todo: DELETE THIS LINE
            pass
            is_equal = np.array_equal(permuted_matrix, matrix)
            is_in_matrices_set = {permuted_matrix} in adj_matrices
            # if is_in_matrices_set and not is_equal:
            #     adj_matrices.remove(permuted_matrix)
            # is_in_matrices_list = any(np.array_equal(permuted_matrix, m) for m in adj_matrices)
    return adj_matrices


# def reduce_graphs2(graphs):
#     adj_matrices = list()
#     # create adjacency matrices
#     for g in graphs:
#         a = np.asmatrix(nx.adjacency_matrix(g))
#         adj_matrices.append(a)
#         # a = get_adjacency_matrix(g)
#     # remove permutations
#     permutation_mateices = mu.generate_all_permutation_matrices(get_n_from_graphs_set(graphs))
#     for mat in adj_matrices:
#         for p in permutation_mateices:
#             permuted_matrix = np.matmul(np.matmul(np.asarray(p), np.asarray(mat)), np.asarray(p.transpose()))
#             print(permuted_matrix)
#             print(permuted_matrix.tolist())
#             if permuted_matrix in adj_matrices and permuted_matrix != mat:
#                 adj_matrices.remove(mat)
#             #     adj_matrices.remove(mat)
