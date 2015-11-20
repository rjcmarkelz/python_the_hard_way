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