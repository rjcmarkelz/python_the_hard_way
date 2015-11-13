# chapter 1 of functional python book
def sum(seq):
    if len(seq) == 0:
        return 0
    return seq[0] + sum(seq[1:])

sum([1, 2, 3, 4, 1])
sum([1])

# recursive
def until(n, filter_func, v):
    if v == n:
        return []
    if filter_func(v):
        return [v] + until(n, filter_func, v+1)
    else:
        return until(n, filter_func, v+1)

# now use lambda for one line functions

mult_3_5 = lambda x: x % 3 == 0 or x % 5 == 0 

mult_3_5(3)
mult_3_5(5)

# combine
until(10, lambda x: x % 3 == 0 or x % 5 == 0, 0)

# nested generator expression
sum(n for n in range(1, 10) if n % 3 == 0 or n % 5 == 0)

# object creation
# plus operator is both commutative and associative
1 + 2 + 3 + 4

# can also be
# fold values left to right
# create intermediate values 3 and 6
((1 + 2) + 3) + 4 

# fold values right to left
# intermediate objects 7 and 9 are created
1 + (2 + (3 + 4)) 

# slight advantage working left to right
import timeit
timeit.timeit("((([] + [1]) + [2]) + [3]) + [4]")
timeit.timeit("[] + ([1] + ([2] + ([3] + [4])))")

####
# Important functional design that + has no hidden side effects
####

# stack of turtles
# CPUs are generally procedural not functional or OO
# three main layers of abstraction
# 1) applications will be functions all the way down until 
#       we hit the objects
# 2) Underlying Python runtime environment that supports functional
#       programming is objects- all the way down- until we hit turtles
# 3) The libraries that support python are a turtle on which python stands
# 
# The OS and hardware form thier own stack of turtles













