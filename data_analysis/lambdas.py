#lambdas 
f = lambda x, y, z: x + y + z
f(2, 30, 400)
L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]

for f in L:
    print(f(3))

print(L[0](11))
