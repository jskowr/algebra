#!/usr/bin/python3
#-*- coding:utf-8 -*-

# Na początku pliku powinien być shebang, czyli sekwencja "#!", a następnie nazwa interpretera.
# Używaj Pythona 3, bo bez trójki domyślnie używasz dwójki.
# Zadeklaruj kodowanie za pomocą konwencji z Emacsa, używając ciągu "-*-".



class Vector:

	#vector = [] # Nie definiuj pola 'vector' tutaj, bo stanie się ono polem statycznym (wspólnym dla wszystkich instancji).

	def __init__(self, vector):
		self.vector = vector
		
	def __str__(self): # Żeby wydrukować obiekt, zdefiniuj mu funkcję __str__, która zwraca string.
		return str(self.vector) # Nie musisz stosować nawiasów wokół return.
		
	def __iadd__(self, second_vector): # Jako że to jest dodawanie w miejscu (+=), zastosuj metodę __iadd__.
		if len(self.vector) != len(second_vector): # Po ifie nie musi być nawiasu. Rób spacje wokół operatorów.
			raise ValueError('Vectors must be the same size.')
		for i in range(len(self.vector)):
			self.vector[i] += second_vector[i]	
	
	def __isub__(self, second_vector): # Jako że jest to odejmowanie w miejscu (-=), zastosuj metodę __isub__.
		if(len(self.vector)!=len(second_vector)):
			raise ValueError('Vectors must be the same size.')
		for i in range(len(self.vector)):
			self.vector[i] -= second_vector[i]		
		
	def __imul__(self, scalar): # Jako że jest to mnożenie przez skalar w miejscu (*=), zastosuj metodę __imul__.
		for i in range(len(self.vector)):
			self.vector[i] *= scalar
			
	def scalar_product(self, second_vector):
		sum_ = 0 # Ponieważ 'sum' jest słowem zarezerwowanym, używaj 'sum_'.
		for i in range(len(self.vector)):
			sum_ += (self.vector[i] * second_vector[i])
		return sum_	


