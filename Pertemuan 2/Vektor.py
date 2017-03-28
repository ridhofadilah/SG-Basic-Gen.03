import numpy as np
M = np.mat("0 0 -2;1 2 1;1 0 3")

eigenvalue,eigenvector = np.linalg.eig(M)
print (eigenvalue)
print ()
print (eigenvector)