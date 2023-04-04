from itertools import chain, combinations


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def format_eigenvalues(eigenvalues):
    eigenvalues = [round(eigenvalue, 4) for eigenvalue in eigenvalues]
    for eigenvalue in eigenvalues:
        if eigenvalue == 0:
            eigenvalue = 0
    return eigenvalues