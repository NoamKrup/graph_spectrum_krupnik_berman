import numpy as np
import itertools
import networkx as nx
from scipy import linalg


def generate_all_permutation_matrices(n):
    permutation_matrices = list()
    for p in itertools.permutations(np.eye(n)):
        perm_mat = np.array(np.matrix(p))
        permutation_matrices.append(perm_mat)
    return permutation_matrices


def format_eigenvalues(eigenvalues):
    eigenvalues = [round(eigenvalue, 4) for eigenvalue in eigenvalues]
    eigenvalues2 = list(map(lambda x: 0 if x == 0 or x == -0 else x, eigenvalues))
    return eigenvalues2


def get_eigenvalues_of_a_matrix(a):
    eigenvalues = linalg.eigh(a, eigvals_only=True)
    # round eigenvalues to 4 decimal places
    eigenvalues = format_eigenvalues(eigenvalues)
    return eigenvalues


def is_matrices_equal(m1, m2):
    is_equal = np.array_equal(m1, m2)
    return is_equal

def remove_matrix_from_list(List, martix):
    ind = 0
    size = len(List)
    while ind != size and not np.array_equal(List[ind], martix):
        ind += 1
    if ind != size:
        List.pop(ind)
    else:
        raise ValueError('array not found in list.')


def get_n_from_matrix_list(List):
    return len(List[0])