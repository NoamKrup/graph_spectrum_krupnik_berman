import numpy as np
import itertools
import networkx as nx


def generate_all_permutation_matrices(n):
    permutation_matrices = list()
    for p in itertools.permutations(np.eye(n)):
        perm_mat = np.matrix(p)
        permutation_matrices.append(perm_mat)
    return permutation_matrices
