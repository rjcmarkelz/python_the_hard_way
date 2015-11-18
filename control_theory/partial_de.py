import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

a = 2.8e-4
b = 5e-3
tau = .1
k = -.005

# size of 2D grid
size = 100 # size of 2D grid
dx = 2./size # space step

T = 10.0 #total time
dt = .9 * dx**2/2 # time step
n = int(T / dt)

U = np.random.rand(size, size)
V = np.random.rand(size, size)

# a = [1:-1,1:-1]
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

    U[1:-1,1:-1], V[1:-1,1:-1] = Uc + dt * (a * deltaU + Uc**3 - Vc + k), Vc + dt * (b * deltaV + Uc - Vc) / tau

    for Z in (U, V):
        Z[0,:] = Z[1,:]
        Z[-1,:] = Z[-2,:]
        Z[:,0] = Z[:,1]
        Z[:,0] = Z[:,-2]

plt.imshow(U, cmap = plt.cm.copper, extent = [-1,1,-1,1]);
plt.xticks([]); plt.yticks([]);



