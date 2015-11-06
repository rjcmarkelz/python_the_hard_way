import scipy.misc
import numpy as np
img = scipy.misc.lena().astype('float32')

scores = np.array([101, 103, 84], dtype = 'float32')
scores

# simplified even further 
scores = np.float32([101,103,84])
scores