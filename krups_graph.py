import graph_utils as gu


class krup_graph:
    def __init__(self, graph):
        self.adjacency_matrix = gu.get_adjacency_matrix_from_graph(graph)