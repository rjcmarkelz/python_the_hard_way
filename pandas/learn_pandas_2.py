# NumPy
import numpy as np 

# compare vectorization
def squares(values):
    result = []
    for v in values:
        result.append(v * v)
return result # something wierd going on here when sending to ipython


to_square = range(100000)
%timeit squares(to_square)

# now with numpy array
array_to_square = np.arange(0, 100000)
%timeit array_to_square ** 2
# also caching?

# create simple arrays
a1 = np.array([1 , 2, 3, 4, 5])
a1
type(a1)
np.size(a1)

# add a float, converts all elements to floats
a2 = np.array([1 , 2, 3, 4.0, 5.0])
a2.dtype

# repeat sequence
a3 = np.array([0]*10)
a3

# convert range to np array
np.array(range(10))

# zeros 
np.zeros(10)
np.zeros(10, dtype = int)

np.arange(0, 10) # 0 to 9
np.arange(0, 10 , 2) # increment by
np.arange(10, 0, -1) # decrement by 1
np.linspace(0, 10, 11) # evenly spaced numbers

# multiply array by 2
a1 = np.arange(0, 10)
a1 * 2

a2 = np.arange(10, 20)
# add two arrays
a1 + a2

#2x2 array
np.array([[1, 2], [3, 4]])

# create 1x20 array and reshape to 5x4 2d array
m = np.arange(0, 20).reshape(5, 4)
m

# product of ALL the dimensions
np.size(m)

# numbe of rows in 2D array
np.size(m, 0)

# number of columns 
np.size(m, 1)

# selecting array elements
# zero based elements
a1[0], a1[2]

# in 2D array row 1 column 2
m[1, 2]

# all items in row 1
m[1, ]

# omit row names with :, DO NOT LEAVE BLANK
m[:, 2]

# items less than 5
a = np.arange(5)
a < 2

# less than 2 or greater than 3?
(a < 2) | (a > 3)

def exp (x):
return x < 3 or x > 3

np.vectorize(exp)(a)

# boolean selection
r = a < 3
a[r]

np.sum(a < 3)

# applied across two arrays
a1 = np.arange(0, 5)
a2 = np.arange(5, 0, -1)
a1 < a2

########
# next up slicing arrays
########
