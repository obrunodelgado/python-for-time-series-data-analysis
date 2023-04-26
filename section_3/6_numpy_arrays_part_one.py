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