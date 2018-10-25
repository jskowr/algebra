#!/usr/bin/python3
#-*- coding:utf-8 -*-


from vector import Vector

list_ = [1,2,3,4,5] # 'list' jest słowem zarezerwowanym, użyj 'list_'.
second_vector = Vector([2,-1,10,9,3]) # Tutaj też chcesz wektora, nie gołej listy.
vec = Vector(list_)

vec.print_vector()

vec.scalar_multiplication(2)

vec.print_vector()

vec.add_vectors(second_vector)

vec.print_vector()

vec.subtract_vectors(second_vector)

vec.print_vector()

scalar_product = vec.scalar_product(second_vector)

print("scalar product:", scalar_product) # Wystarczy przecinek, nie musisz dodawać stringów.


