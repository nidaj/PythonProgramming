"""
Program for 2D array multiplication
"""
from numpy import *


def accept_matrix():
    row = int(input("Enter number of rows for first matrix "))
    col = int(input("Enter number of column for first matrix "))
    matric = []
    for r in range(row):
        arr = []
        for c in range(col):
            arr.append(int(input()))
        matric.append(arr)
    return matric


def matrix_multiply(mat1, mat2):
    """

    :rtype: matrix
    """
    mat3 = matrix(mat1) * matrix(mat2)
    return mat3


try:
    matric1 = accept_matrix()
    matric2 = accept_matrix()
    dot_product = matrix_multiply(matric1, matric2)
    print(dot_product)
except Exception as e:
    print(e)
