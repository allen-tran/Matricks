import numpy as np
from get_matrix import instantiate_matrix
from numpy.linalg import eig

def eigen():
    a = instantiate_matrix()
    u = len(a)

    for i in range(u):
        for j in range(len(a[i])):
            x = int(input("Enter element: "))
            a[i][j] = x

    print("\nMatrix:")
    print(np.asmatrix(a))
    print("\n\nResult:")
    print(eig(a))

eigen()
