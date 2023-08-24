import numpy as np
import sympy

# Create a random matrix A
A = np.random.randint(-9, 9, (3, 3))
A[:, 2] = A[:, 0]
print('A =\n', A)

# Convert the numpy array to the sympy.Matrix class
A_sympy = sympy.Matrix(A)
print(A_sympy)

# Calculate the RREF of A
# `rref` returns the reduced row echelon form and the pivot columns
A_rref = A_sympy.rref()
print('A_rref (from sympy):\n', A_rref)

# Convert A_rref to numpy
A_rref = np.array(A_rref[0].tolist()) # first convert to list format
print('A_rref =\n', A_rref)
