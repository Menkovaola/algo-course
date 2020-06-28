def swap(array, a, b):
    buf = array[a]
    array[a] = array[b]
    array[b] = buf


def partition(array, l, r):
    x = (l + r) // 2
    swap(array, l, x)
    j = l
    for i in range(l + 1, r + 1):
        if array[i] < array[l]:
            j += 1
            swap(array, i, j)
    swap(array, l, j)
    return j


def quick_sort(array, l, r):
    if l < r:
        m = partition(array, l, r)
        quick_sort(array, l, m)
        quick_sort(array, m + 1, r)


def quick_sort_helper(array):
    length = len(array)
    quick_sort(array, 0, length - 1)
    return array


print(quick_sort_helper([2, 6, 7, 3, 9, 2, 1]))
print(quick_sort_helper([3]))
print(quick_sort_helper([3, 2, 1]))
print(quick_sort_helper([3, 6, 3, 3, 3, -1000, 35]))
print(quick_sort_helper([3, 6, 3, 3, 3, -1000, 35]))
