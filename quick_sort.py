import random


def swap(array, a, b):
    buf = array[a]
    array[a] = array[b]
    array[b] = buf


def partition(array, l, r):
    x = (l+r)//2
    swap(array, l, x)
    j = l
    for i in range(l + 1, r + 1):
        if array[i] <= array[l]:
            j += 1
            swap(array, i, j)
    swap(array, l, j)
    return j


def quicksort(array, l, r):
    if l < r:
        m = partition(array, l, r)
        quicksort(array, l, m)
        quicksort(array, m+1, r)


s = [2, 6, 7, 3, 9, 2, 1]
quicksort(s, 0, len(s) - 1)
print(*s)