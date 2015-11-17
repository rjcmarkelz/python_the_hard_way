import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

a = 2.8e-4
b = 5e-3
tau = .1
k = -0.005

# size of 2D grid
size = 100 # size of 2D grid
dx = 2.0/size # space step

T = 10.0 #total time
dt = 0.9 * dx**2/2 # time step
n = int(T / dt)

U = np.random.rand(size, size)
V = np.random.rand(size, size)
U
a = [1:-1,1:-1]
# calculate laplacian
def lapalacian(Z):
    Ztop = Z[0:-2, 1:-1]
    Zleft = Z[1:-1, 0:-2]
    Zbottom = Z[2: , 1:-1]
    Zright = Z[1:-1, 2: ]
    Zcenter = Z[1:-1, 1:-1]
    return (Ztop + Zleft + Zbottom + Zright - 4 * Zcenter)/ dx**2

for i in range(n):
    deltaU = lapalacian(U)
    deltaV = lapalacian(V)
    Uc = U[1:-1,1:-1]
    Vc = V[1:-1,1:-1]




