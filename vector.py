class Vector:

	vector = []

	def __init__(self, vector):
		self.vector = vector
		
	def print_vector(self):
		print(self.vector)
		
	def add_vectors(self, second_vector):
		if(len(self.vector)!=len(second_vector)):
			raise ValueError('Vectors must be the same size.')
		for i in range(len(self.vector)):
			self.vector[i] += second_vector[i]	
	
	def subtract_vectors(self, second_vector):
		if(len(self.vector)!=len(second_vector)):
			raise ValueError('Vectors must be the same size.')
		for i in range(len(self.vector)):
			self.vector[i] -= second_vector[i]		
		
	def scalar_multiplication(self, scalar):
		for i in range(len(self.vector)):
			self.vector[i] *= scalar
			
	def scalar_product(self, second_vector):
		sum=0
		for i in range(len(self.vector)):
			sum+=(self.vector[i]*second_vector[i])
		return sum	