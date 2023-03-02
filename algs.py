def swap(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

def sort2(l):
    assert len(l) == 2

    if l[0] > l[1]: swap(l, 0, 1)

def sort3(l):
    assert len(l) == 3

    if l[0] > l[1]: swap(l, 0, 1)
    if l[1] > l[2]:
        swap(l, 1, 2)
        if l[0] > l[1]: swap(l, 0, 1)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]