import numpy as np

def gram_schmidt(A):
    U = np.zeros(A.shape)
    U[:, 0] = A[:, 0] / np.linalg.norm(A[:, 0])
    for i in range(1, A.shape[1]):
        U[:, i] = A[:, i]
        for j in range(i-1):
            U[:, i] = U[:, i] - (U[:, j].T @ U[:, i]) / (np.linalg.norm(U[:, j]))**2 * U[:, j]
        U[:, i] = U[:, i] / np.linalg.norm(U[:, i])

    return U

A = np.array([[1, 1, 1],
              [1/1000, 1/1000, 0],
              [1/1000, 0, 1/1000]])

U = gram_schmidt(A)

print(U)

# Orthogonality test
u1_u2_dot = U[:, 0].T @ U[:, 1]
print(f'u1.T @ u2 = {u1_u2_dot}')

u1_u3_dot = U[:, 0].T @ U[:, 2]
print(f'u1.T @ u3 = {u1_u3_dot}')
