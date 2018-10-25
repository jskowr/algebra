#!/usr/bin/python3
#-*- coding:utf-8 -*-

class Matrix:

	def __init__(self, matrix):
		self.matrix = matrix
		
	def __str__(self):
		return str(self.matrix)
		
	def __imul__(self, scalar):
		for a in range(len(self.matrix)):
			for b in range(len(self.matrix[a])):
				self.matrix[a][b] *= scalar
				
	def __iadd__(self, second_matrix):
		if(len(self.matrix) != len(second_matrix) || len(self.matrix[0]) != len(second_matrix[0])):
			raise ValueError('Matrixes must be the same size.')
		for a in range(len(self.matrix)):
	
			for b in range(len(self.matrix[a])):
				self.matrix[a][b] += second_matrix[a][b]
				
	def __isub__(self, second_matrix):
		if(len(self.matrix) != len(second_matrix) || len(self.matrix[0]) != len(second_matrix[0])):
			raise ValueError('Matrixes must be the same size.')
		for a in range(len(self.matrix)):
			for b in range(len(self.matrix[a])):
				self.matrix[a][b] += second_matrix[a][b]

	def __matmul__(self, second_matrix):
		pass
				