#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    Temp = []
    for i in range(len(matrix)):
        Temp = list(map(lambda x: x ** 2, matrix[i]))
        new_list.append(Temp)
    return new_list
