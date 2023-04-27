import numpy as np

arr = np.arange(0, 10)

print(arr + 100)

print(arr / 100)

print(arr ** 2)

print((arr + 2) / 100)

print(arr + arr)

print(np.sqrt(arr))

print(np.log(arr))

print(np.sin(arr))

print(arr.sum())

print(arr.mean())

print(arr.max())

print(arr.min())

print(arr.std())

print(arr.var())

arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(arr_2d.sum())

print(arr_2d.sum(axis=0))  # sum of columns across rows

print(arr_2d.sum(axis=1))  # sum of rows across columns