#!/usr/bin/env python
# find horizontal, vertical and diagonal
# lines equal list of elements

import sys
import os

matrix_d = [[1, 2, 8, 2],
            [3, 2, 1, 2],
            [2, 6, 7, 2],
            [5, 4, 3, 0]]

# rotate matrix 90 degree rights
matrix_t = [list(i) for i in zip(*matrix_d[::-1])]

matrix_sum = [matrix_d, matrix_t]

# diamond matrix row number (also 0)
n_diam = (len(matrix_d)-1)*2-1

def equal_list(elements) :
    """ sequence of equal elements """
    counter = 1 
    i = -1
    for j in elements :
        if j == i :
            counter += 1
            if counter == 3 :
                return True
        else :
            counter = 1            
        i = j
    return False

def iterate_cells(matrix) :
    """ matrix diamond iterate """
    n = len(matrix)
    for i in range(n) :
        matrix_diam = []
        for j in range(i+1) :
            matrix_diam.append(matrix[j][i-j])
        if(equal_list(matrix_diam)):
            return True
    for i in range(1, n) :
        matrix_diam = []
        for j in range(n-i) :
            matrix_diam.append(matrix[i+j][n-j-1])
        if(equal_list(matrix_diam)) :
            return True
    for i in matrix :
        if(equal_list(i)) :
            return True

for i in matrix_sum :
    print(iterate_cells(i))

