def example(a, b, **kw):
    return a*b

type(example)

# although NOT recommended, can use lambdas
mersenne = lambda x: 2**x-1

# combine functions with higher order functions
# immutable data
## a common design pattern that works well with immutable objects: the wrapper()
## 
snd = lambda x: x[1]
snd(max(map(lambda yc: (yc[1],yc), year_cheese)))

# strict and non-strict evals
0 and print("right")
True and print("right")

# tail call optimization
# know there are limits to 1000 recursions by default in python
import math
def isprime(p):
    if p < 2: return False
    if p == 2: return True
    if p % 2 == 0: return False
    return not any(p == 0 for p in range(3, int(math.sqrt(p))+ 1, 2))

isprime(10)
isprime(23)