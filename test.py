#!/usr/bin/python3
#-*- coding:utf-8 -*-

#metody __len__, __getitem__, __setitem__, __add__, __sub__, __mul__, __rmul__ i __matmul__

from vector import Vector
from matrix import Matrix
import random

row = 5
col = 7

matrix = [None] * row

for x in range(5):
	matrix[x] = [None] * col
	for y in range(7):
		matrix[x][y] = random.randint(-5, 5) 

matrix = Matrix(matrix)

print(matrix.__str__())

matrix.__imul__(3)

print(matrix.__str__())


