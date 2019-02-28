import numpy as np

# part 1
name = 'Ran Liao'
extension_id = 'X154149'
print("I'm " + name + ", and my extension id is " + extension_id + ".")

# part 2
A = np.matrix(np.random.rand(3, 5))
print(A)
print(type(A))

# part 3
A_size = A.size
A_shape = A.shape
print(A_size)
print(A.shape)

# part 4
A = A[:, :4]
print(A)

# part 5
B = A.T
print(B)

# part 6
b_min = np.min(B[:, 0])
print(b_min)

# part 7
a_min = np.min(A)
a_max = np.max(A)
print(a_min, a_max)

# part 8
X = np.random.rand(4)
print(X)
print(type(X))

# part 9/10
def foo(A, X):
    D = A * np.matrix(X).T
    print(D)
foo(A, X)

# part 11
Z = complex(np.random.rand(1), np.random.rand(1))
print(Z)
print(np.absolute(Z))

