import numpy as np

mylist = [1, 2, 3]

print(mylist)
print(type(mylist))

myArray = np.array(mylist)

print(myArray)
print(type(myArray))

arrange = np.arange(0, 10, 2)
print(arrange)

print(np.zeros(shape=(4, 5)))

print(np.ones(shape=(2, 3)))

np.random.seed(101)
arr = np.random.randint(0, 100, 10)
print("Values in arr: ", arr)
arr2 = np.random.randint(0, 100, 10)
print(arr2)
print("Max value: ", arr.max())
print("Index of max value in arr: ", arr.argmax())
print("Index of min value in arr: ", arr.argmin())
print("Mean value of arr: ", arr.mean())
print("Reshape of arr", arr.reshape(5, 2))

# reshape (height,width)

mat = np.arange(0, 100).reshape(10, 10)
print("New mat: ", mat)
print("Shape of mat: ", mat.shape)

row = 2
col = 2
print(mat[row, col])
print(mat[:, 2])

matCopy = mat
print(matCopy)

print(matCopy[0:3, 0:3])
matCopy[0:3, 0:3] = 0
print(matCopy[0:3, 0:3])
print(matCopy)
