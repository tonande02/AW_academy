import numpy as np

# arr = np.array(
#     [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#     [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
#     [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
# print(arr)

# print(type(arr))
# print(arr.ndim)
# print(arr[0, 1, 2])
# print(arr[-1, -1, -1])
# print(arr.shape)
# print(arr.size)


arr1 = np.array(
    [[[1], [2], [3]],
    [[4], [5], [6]],
    [[7], [8], [9]]])

print(arr1)
print()

print(np.argmax(arr1))
print(np.tile(arr1, reps=3))