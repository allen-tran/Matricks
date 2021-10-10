import numpy as np
from get_matrix import instantiate_matrix

def sub():
    a = instantiate_matrix()
    u = len(a)

    for i in range(u):
        for j in range(len(a[i])):
            x = int(input("Enter element: "))
            a[i][j] = x
    
    b = instantiate_matrix();
    
    v = len(b)

    for i in range(v):
        for j in range(len(b[i])):
            x = int(input("Enter element: "))
            b[i][j] = x

    print("\nMatrix A:")
    print(np.asmatrix(a))
    print("\nMatrix B:")
    print(np.asmatrix(b))
    print("\n\nResult: ")
    print(np.sub(a, b))

sub()