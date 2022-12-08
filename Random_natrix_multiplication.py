from numpy import random
print('Nhap kich thuoc ma tran : ')
n = int(input())
A = random.rand(n, n) * 10
B = random.rand(n, n) * 10


def matrix_mul(x, y):
    z = x
    for i in range(n):
        for j in range(n):
            t = 0
            for k in range(n):
                t = t + x[i][k] * y[k][j]
            z[i][j] = t
    return z


print('Ma tran thu nhat : \n', A)
print('Ma tran thu hai \n', B)
C = matrix_mul(A, B)
print('Tich cua hai ma tran la : \n', C)
