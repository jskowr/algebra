#!/usr/bin/python3
#-*- coding:utf-8 -*-

#metody __len__, __getitem__, __setitem__, __add__, __sub__, __mul__, __rmul__ i __matmul__

from vector import Vector

list_ = [1,2,3,4,5] # 'list' jest słowem zarezerwowanym, użyj 'list_'.
second_vector = Vector([2,-1,10,9,3]) # Tutaj też chcesz wektora, nie gołej listy.
vec = Vector(list_)

print(vec.__len__())


