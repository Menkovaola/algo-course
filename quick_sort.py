def swap(array, a, b):
    buf = array[a]
    array[a] = array[b]
    array[b] = buf


def partition(array, l, r, y):
    x = (l + r) // 2
    swap(array, l, x)
    j = l
    k=l
    for i in range(l + 1, r + 1):
        if array[i][y] < array[l][y]:
            j += 1
            swap(array, i, j)
        if array[i][y] == array[l][y]:
            k += 1
            j += 1
            swap(array, i, k)
    s = j - k
    for i in range(k+1):
        swap(array, k, s)
        s=s+1
    return j-k,j

def quick_sort(array, l, r, y):
    while l < r:
        n,m = partition(array, l, r, y)
        quick_sort(array, l, n-1, y)
        l=m+1

def quick_sort_helper(array, y):
    length = len(array)
    quick_sort(array, 0, length - 1, y)
    return array

listik = []
n, m = map(int,input().split())
for i in range(n):
    listik.append(list(map(int, input().split())))
dots=list(map(int,input().split()))

sortedBeg = quick_sort_helper(listik, 0)
sortedEnd = quick_sort_helper(listik, 1)

for dot in dots:
    case = []
    for j in range(len(sortedBeg)):
        if sortedBeg[j][0]<= dot:
            case.append(sortedBeg[j])
    for k in range(len(sortedEnd)):
        if sortedEnd[k][1]< dot:
            case.remove(sortedEnd[k])
    print (len(case),end=' ')


