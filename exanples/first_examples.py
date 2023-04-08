import networkx as nx

def create_simple_graph_with_edges(edges):
    g = nx.Graph()
    g.add_nodes_from([1, 2, 3, 4])
    g.add_edges_from(edges)
    return g

