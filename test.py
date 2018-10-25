from vector import Vector

list = [1,2,3,4,5]
second_vector = [2,-1,10,9,3]
vec = Vector(list)

vec.print_vector()

vec.scalar_multiplication(2)

vec.print_vector()

vec.add_vectors(second_vector)

vec.print_vector()

vec.subtract_vectors(second_vector)

vec.print_vector()

scalar_product = vec.scalar_product(second_vector)

print("scalar product: "+str(scalar_product))