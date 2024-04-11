import numpy as np
# arr_01 = np.array([2, 4, 6, 'Pawan'], dtype='<U32')
# print(arr_01)

# arr_02 = np.array([0, 1, 2, 3, 4])
# print(f'1st item:{arr_02[0]}')
# print(f'2nd item:{arr_02[1]}')
# print(f'3rd item:{arr_02[2]}')
# print(f'4th item:{arr_02[3]}')

# arr_idx_2d = np.array([
#     [11, 12, 13],
#     [21, 22, 23],
#     [31, 32, 33]
# ])

# print(arr_idx_2d[0, 0])
# print(arr_idx_2d[0, 1])
# print(arr_idx_2d[0, 2])
# print(arr_idx_2d[1, 0])
# print(arr_idx_2d[1, 1])
# print(arr_idx_2d[1, 2])
# print(arr_idx_2d[2, 0])
# print(arr_idx_2d[2, 1])
# print(arr_idx_2d[2, 2])

# arr_02 = np.array([1, 2, 3, 4, 5, 6, 7])
# arr_slice = arr_02[1:5]
# print(arr_slice)
# arr_slice4 = arr_02[4:]
# print(arr_slice4)
# arr_slice2 = arr_02[::2]
# print(arr_slice2)
# arr_sliceback = arr_02[-3:-1]
# print(arr_sliceback)
# arrreverse = arr_02[::-1]
# print(arrreverse)


# arr2d = np.array([
#     [11, 12, 13],
#     [21, 22, 23],
#     [31, 32, 33]
# ])
# # print(arr2d[1:])
# arr2dslice = arr2d[:, 1]
# print(arr2dslice)
# arr2dslice11 = arr2d[1, 1:]
# print(arr2dslice11)

# base_arr = np.array([0, 1, 2, 3, 4, 5, 6])
# print(base_arr)

# copy_arr = base_arr.copy()

# print(copy_arr)
# print(f"do orginal array: {np.shares_memory(base_arr, copy_arr)}")

# arr_03 = np.array([1, 2, 3, 4, 5, 6, 7])
# split_array = np.array_split(arr_03, 3)
# print("Split Array:\n", split_array)


# split_array_2d = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12],
#     [],
#     []
# ])
# np.array_split(split_array_2d, 3)
# print(split_array_2d)
# np.array_split(split_array_2d, 3, axis=1)
# print(split_array_2d)
# x1 = np.arange(1, 10000000)
# x2 = np.arange(1, 10000000)
# null = np.zeroes(x1.shape)
# start_time = time.process_time()
# for i in range(len(x1)):
#   mul[i] = x1[i]*x2[i]
# end_time = time.process_time()

# a = np.array([1, 2, 3])
# b =2
# print(a+b)
a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]])
print(f"shape of a: {a}")
print(f"shape of b: {b}")
print
