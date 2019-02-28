import numpy as np

# 1 Include a sec4on with your name
name = 'Ran Liao'
extension_id = 'X154149'
print("I'm " + name + ", and my extension id is " + extension_id + ".")

# 2 Create matrix A with size (3,5) containing random numbers
A = np.matrix(np.random.rand(3, 5))
print(A)
print(type(A))

# 3 Find the size and length of matrix A
A_size = A.size
A_shape = A.shape
print(A_size)
print(A.shape)

# 4 Resize (crop/slice) matrix A to size (3,4)
A = A[:, :4]
print(A)

# 5 Find the transpose of matrix A and assign it to B
B = A.T
print(B)

# 6 Find the minimum value in column 1 of matrix B
b_min = np.min(B[:, 0])
print(b_min)

# 7 Find the minimum and maximum values for the en4re matrix A
a_min = np.min(A)
a_max = np.max(A)
print(a_min, a_max)

# 8 Create vector X (an array) with 4 random numbers
X = np.random.rand(4)
print(X)
print(type(X))


# 9 Create a func4on and pass vector X and matrix A in it
# 10 In the new func4on mul4ply vector X with matrix A and assign the result to D
def foo(A, X):
    D = A * np.matrix(X).T
    print(D)
    return D


D = foo(A, X)

# 11 Create a complex number Z with absolute and real parts != 0
Z = complex(np.random.rand(1), np.random.rand(1))
print(Z)

# 12 Show its real and imaginary parts as well as it’s absolute value
print("real part :", Z.real)
print("imaginary part :", Z.imag)
print("absolute value :", np.absolute(Z))

# 13 Mul4ply result D with the absolute value of Z and record it to C
C = D * np.absolute(Z)
print(C)

# 14 Convert matrix B from a matrix to a string and overwrite B
B = np.array2string(B)
print(B)

# 15 Display a text on the screen: ‘Name is done with HW2‘, but pass your ‘Name’ as a string variable 
print(name, "is done with HW2")
