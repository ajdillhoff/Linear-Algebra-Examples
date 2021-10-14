import numpy as np
import scipy.linalg as linalg

# Create a random 4x4 matrix
A = np.random.randint(-9, 9, (3, 3))
print('Matrix A\n', A)

# Compute the determinant of A
detA = linalg.det(A)
print('determinant of A\n', detA)

# Compute the inverse of A
invA = linalg.inv(A)
print('inverse of A\n', invA)

# Compute the rank of A
# Note the use of numpy
rankA = np.linalg.matrix_rank(A)
print('rank of A\n', rankA)

# Compute the null space of A
nullA = linalg.null_space(A)
print('Null space\n', nullA)

# Solve the matrix equation Ax=b
b = np.random.randint(-9, 9, (3, 1))
print('b vector\n', b)

x = linalg.solve(A, b)
print('solved x vector\n', x)

print('A@x =\n', A@x)
