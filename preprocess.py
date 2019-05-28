from codingBinary.binary_3_gvcclt import *
from featureExtration import *

#Wczytywanie zbiorow
read_examples()

print("PCA w trakcie!")

X = pca()
Y = np.array(data)
# print("X: ", X)
# print("Y: ", Y)

np.save("inputs3_gvcclt.npy", X)
np.save("labels3_gvcclt.npy", Y)


# print(X.shape[0], Y.shape[0])

print("PCA gotowe!")