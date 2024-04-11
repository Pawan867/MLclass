
def linear_search(arr, value):
    for i, item in enumerate(arr):
        if item == value:
            return i
    return -1


def binary_search(arr, value):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def linear_search_2d(arr, value):
    for i, row in enumerate(arr):
        for j, item in enumerate(row):
            if item == value:
                return (i, j)
    return -1


def linear_search_3d(arr, value):
    for i, matrix in enumerate(arr):
        for j, row in enumerate(matrix):
            for k, item in enumerate(row):
                if item == value:
                    return (i, j, k)
    return -1


if __name__ == "__main__":
    # 1D array search
    arr_1d = [10, 20, 30, 40, 50]
    print("Linear Search in 1D:", linear_search(arr_1d, 30))
    print("Binary Search in 1D:", binary_search(sorted(arr_1d), 30))

    # 2D array search
    arr_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Linear Search in 2D:", linear_search_2d(arr_2d, 5))

    # 3D array search
    arr_3d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    print("Linear Search in 3D:", linear_search_3d(arr_3d, 7))
