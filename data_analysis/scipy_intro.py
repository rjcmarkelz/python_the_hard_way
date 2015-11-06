import scipy.misc
img = scipy.misc.lena()
import matplotlib.pyplot as plt

plt.gray()
plt.imshow(img)
plt.show()

# slice the image
img[0:3, 0:7]

# change the entries
img[1,1:6] = 0

#print the changed results
print(img[0:3,0:7])

# examine object atributes
img.dtype, img.shape, img.size

