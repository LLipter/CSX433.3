import numpy as np

# part 1
name = 'Ran Liao'
extension_id = 'X154149'
print("I'm " + name + ", and my extension id is " + extension_id + ".")

# part 2
A = np.matrix(np.random.rand(3, 5))
print(A)
# print(type(A))

# part 3
A_size = A.size
A_shape = A.shape
# print(A_size)
# print(A.shape)

# part 4
A = A[:, :4]
print(A)
