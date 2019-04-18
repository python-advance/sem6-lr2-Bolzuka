# Реализуйте перемножение квадратных матриц произвольной размерности,
# используя библиотеку numpy (для создания матриц) и библиотеку threading
# (поточное вычисление).

import pytest
import numpy
import threading

A = numpy.array([[2,1],[2,1]])
B = numpy.array([[1,3],[1,3]]) #транспонированная матрица B
C = numpy.array([[0,0],[0,0]])

def matrix(a,b,i):
    for j in range (len(A)):
        C[i][j] = sum(map(lambda x,y: x*y, a[i], b[j]))

for j in range (len(A)):
     threading.Thread(target=matrix, args=(A,B,j)).start()

print(C)