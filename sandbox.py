import graph_utils as gu
import matplotlib.pyplot as plt
import networkx as nx


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
