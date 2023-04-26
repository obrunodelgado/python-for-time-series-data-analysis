import numpy as np

mylist = [1, 2, 3]

x = np.array(mylist)

print(x)

print(type(x))

mylist2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

mymatrix = np.array(mylist2)

print(mylist2)

print(mymatrix.shape)

mynewmatrix = np.array(mylist2)

print(np.arange(0, 10))

print(np.arange(0, 10, 2))

print(np.zeros(5))

print(np.zeros((4,10)))

print(np.ones((4,10)))

print(np.ones((5, 5)) + 4)

print(np.ones(4) * 100)

print(np.linspace(0, 10, 100))

print(np.eye(4))

print(np.random.rand(4))

print(np.random.rand(5,5))

print(np.random.randn(2)) # standard normal distribution

print(np.random.randint(1, 100))

print(np.random.randint(1,100,10))

np.random.seed(555)
print(np.random.rand(4))
print(np.random.rand(4))
print(np.random.rand(4))

arr = np.arange(25)
print(arr)

ranarr = np.random.randint(0, 50, 10)
print(ranarr)

print(arr.shape)

print(arr.reshape(5,5))

print(ranarr.max())

print(ranarr.min())

print(ranarr.argmax()) # index location of max value

print(ranarr.argmin()) # index location of min value

print(arr.dtype)
