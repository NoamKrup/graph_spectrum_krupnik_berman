from itertools import chain, combinations
import os

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def print_to_file(file_name, text):
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    if os.path.exists(file_name):
        os.remove(file_name)
    open(file_name, "x")
    with open(file_name, 'w') as f:
        f.write(text)

def print_eigenvalues_counter_to_file(eigenvalues_counter, n):
    file_name = f'outputs/{n}_vertices_eigenvalues_counter.txt'
    text = f'---------- {n} vertices graphs eigenvalues Equivalence classes ----------\n'
    i = 1
    for eigenvalues, count in eigenvalues_counter.items():
        text += f'------ class {i} -----------\n'
        text += f'eigenvalues : {str(eigenvalues)} , count = {count}\n'
        i += 1
    print_to_file(file_name, text)