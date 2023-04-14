import os
import graph_utils as gu
import matrix_utils as mu
import arithmetic_utils as au
import networkx as nx

def print_to_file(file_name, text):
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    if os.path.exists(file_name):
        os.remove(file_name)
    open(file_name, "x")
    with open(file_name, 'w') as f:
        f.write(text)


def print_eigenvalues_counter_of_graph_to_file(graphs):
    n = gu.get_n_from_graphs_set(graphs)
    eigenvalues_counter = au.get_n_vertices_eigenvalues_multy_set(graphs)
    file_name = f'outputs/{n}_vertices_eigenvalues_counter.txt'
    text = f'---------- {n} vertices graphs eigenvalues Equivalence classes ----------\n'
    i = 1
    for eigenvalues, count in eigenvalues_counter.items():
        text += f'------ class {i} -----------\n'
        text += f'eigenvalues : {str(eigenvalues)} , count = {count}\n'
        i += 1
    print_to_file(file_name, text)


def print_eigenvalues_counter_to_file(martices):
    n = mu.get_n_from_matrix_list(martices)
    eigenvalues_counter = au.get_eigenvalues_counter_of_matrix_set(martices)
    file_name = f'outputs/{n}_vertices_eigenvalues_counter.txt'
    text = f'---------- {n} vertices graphs eigenvalues Equivalence classes ----------\n'
    i = 1
    for eigenvalues, count in eigenvalues_counter.items():
        text += f'------ class {i} -----------\n'
        text += f'eigenvalues : {str(eigenvalues)} , count = {count}\n'
        i += 1
    print_to_file(file_name, text)


def print_all_graphs_to_file(graphs):
    n = gu.get_n_from_graphs_set(graphs)
    text = ''
    graph_counter = 1
    file_name = f'outputs/graphs_{n}_vertices.txt'
    for g in graphs:
        text += format_graph_for_printing(g, graph_counter)
        graph_counter += 1
    print_to_file(file_name, text)


def get_reduced_graphs_and_print_to_file(graphs):
    n = gu.get_n_from_graphs_set(graphs)
    reduced_graphs_matrices = gu.reduce_graphs(graphs)
    text = ''
    graph_counter = 1
    file_name = f'outputs/reduced_graphs_{n}_vertices.txt'
    for matrix in reduced_graphs_matrices:
        text += format_matrix_for_printing(matrix, graph_counter)
        graph_counter += 1
    print_to_file(file_name, text)
    return reduced_graphs_matrices


def print_reduced_graphs_eigenvalues_to_file(graphs):
    n = gu.get_n_from_graphs_set(graphs)
    reduced_graphs = gu.reduce_graphs(graphs)


# def print_all_data_for_n_vertices_graphs(n):
#     graphs = gu.create_all_graphes_with_n_vertices(n)
#     reduced_graphs = gu.reduce_graphs(graphs)
#     text = ''
#     graph_counter = 1
#     file_name = f'outputs/all_data_{n}_vertices.txt'
#     for g in graphs:
#         text += gu.format_graph_for_printing(g, graph_counter)
#         graph_counter += 1
#     print_to_file(file_name, text)


def format_matrix_for_printing(matrix, name):
    formated_matrix = f'{matrix}'.replace("[", "").replace("]", "").replace("\n ", "\n")
    eigenvalues = mu.get_eigenvalues_of_a_matrix(matrix)
    formated_eigenvalues = mu.format_eigenvalues(eigenvalues)
    text = f'------ graph {name} -----------\n'
    text += f'Adjacency matrix :\n{formated_matrix}\n'
    text += f'Eigenvalues : {formated_eigenvalues}\n\n'
    return text


def format_graph_for_printing(g, name):
    adjacency_matrix = gu.get_adjacency_matrix(g)
    return format_matrix_for_printing(adjacency_matrix, name)
