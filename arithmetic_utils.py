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
