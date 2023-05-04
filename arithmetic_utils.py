from itertools import chain, combinations
import os
from collections import Counter
import numpy as np
import matrix_utils as mu

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def create_all_zero_one_verctors_of_length_n(n):
    return list(powerset(range(n)))

def get_eigenvalues_counter_of_matrix_set(matrices):
    eigenvalues_counter = Counter()
    matrices_counter = 1
    for m in matrices:
        eigenvalues = mu.get_eigenvalues_of_a_matrix(m)
        eigenvalues_tuple = [tuple(eigenvalues)]
        eigenvalues_counter.update(eigenvalues_tuple)
        matrices_counter += 1
    return eigenvalues_counter
