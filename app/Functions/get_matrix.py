import numpy as np

def instantiate_matrix():
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))
    a = np.zeros((m, n), dtype=int)
    return a