from pylab import *
n = int(ceil((10.0-0.0)/0.1)+1)
x = zeros((n,1), float)

x[0] = 0.0
x[0]

for i in range(n):
    x[i] = i*0.1

print(x)

# write a small script that also plots
from pylab import *
x0 = 0.0; x1 = 10.0; dx = 0.1
n = int(ceil((x1-x0)/dx) + 1)
x = zeros((n,1), float)
y = zeros((n,1), float)

for i in range(n):
    x[i] = x0 + i*dx
    y[i] = sin(x[i])

plot(x,y)
show()

# vectorization
x = linspace(0, 10, 10)
print(x)
x = arange(0.0, 10.0, 0.3)
x = linspace(0,10,10)
y = sin(x)
plot(x,y); show()

x = linspace(0, 10, 1000)
y = sin(x)
hold('on')
plot(x, y, ':')
hold("off")
show()

# using vectorization you can translate equations almost directly into python
x = linspace(0, 10, 1000)
a = 1.0
f = x**2*exp(-a*x)*sin(pi*x)
plot(x, f); show()
