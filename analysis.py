import time
def bubble_sort(arr):
    start = time.time()
    n = len(arr)
    comparison_num = 0
    swap_num = 0

    for i in range(n):
        for j in range(n - i - 1):
            comparison_num += 1
            if arr[j] > arr[j + 1]:
                swap_num += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end = time.time()
    return (comparison_num, swap_num, end - start)

def selection_sort(arr):
    start = time.time()
    n = len(arr)
    comparison_num = 0
    swap_num = 0

    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            comparison_num += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        swap_num += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    end = time.time()
    return (comparison_num, swap_num, end - start)

count_number = 0
def merge_sort(arr):
    global count_number
    count_number = 0
    return merge(arr)

def merge(arr):
    start = time.time()
    if len(arr) <= 1:
        return (0,0,0)

    # divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # recursively sort the left and right halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # merge the two sorted halves
    merged = []
    i, j = 0, 0
    while i < len(left_sorted) and j < len(right_sorted):
        global count_number
        count_number += 1
        if left_sorted[i] < right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1
    merged += left_sorted[i:]
    merged += right_sorted[j:]

    end = time.time()
    return (count_number,count_number,end - start)


def quick_sort(arr):
    global count_number
    count_number = 0
    start = time.time()
    quick(arr)
    end = time.time()
    return (count_number,count_number,end - start)

def quick(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start < end:
        pivot = partition(arr, start, end)
        quick(arr, start, pivot - 1)
        quick(arr, pivot + 1, end)
    return arr

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            global count_number
            count_number += 1
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


# def insertion_sort(arr):
#     start = time.time()
#     num = 0
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         num += 1
#
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#
#     end = time.time()
#     return (num, num, end - start)

def insertion_sort(arr):
    num = 0
    start = time.time()
    for i in range(1,len(arr)):
        j = i
        while j > 0:
            num += 1
            if arr[j] < arr[j-1]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            j -= 1
    end = time.time()
    return (num, num, end - start)


    #generate test lists
import random
def generate_random_list(size):
    return [random.randint(0, 100) for _ in range(size)]

def generate_sorted_list(size):
    return [i for i in range(size)]

def generate_reversed_list(size):
    return [i for i in range(size, 0, -1)]

def generate_nearly_sorted_list(size):
    lst = generate_sorted_list(size)
    # randomly swap a few pairs of adjacent elements
    for _ in range(size // 10):
        i = random.randint(0, size - 2)
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

def generate_duplicate_list(size):
    lst = generate_random_list(size)
    # randomly duplicate some elements
    for _ in range(size // 10):
        i = random.randint(0, size - 1)
        lst.insert(i, lst[i])
    return lst

#test
def test(size):
    lst1 = generate_random_list(size)
    t1 = bubble_sort(lst1)
    t2 = selection_sort(lst1)
    t3 = insertion_sort(lst1)
    t4 = quick_sort(lst1)
    t5 = merge_sort(lst1)
    print("\nrandom_list:")
    print(f"bubble_sort:    list_size = {size} comparisons = {t1[0]} swaps = {t1[1]}    elapsed_time: {t1[2]:7f}")
    print(f"selection_sort: list_size = {size} comparisons = {t2[0]} swaps = {t2[1]}    elapsed_time: {t2[2]:7f}")
    print(f"insertion_sort: list_size = {size} comparisons = {t3[0]} swaps = {t3[1]}    elapsed_time: {t3[2]:7f}")
    print(f"quick_sort:     list_size = {size} comparisons = {t4[0]} swaps = {t4[1]}    elapsed_time: {t4[2]:7f}")
    print(f"merge_sort:     list_size = {size} comparisons = {t5[0]} swaps = {t5[1]}    elapsed_time: {t5[2]:7f}")

    lst2 = generate_sorted_list(size)
    t1 = bubble_sort(lst2)
    t2 = selection_sort(lst2)
    t3 = insertion_sort(lst2)
    t4 = quick_sort(lst2)
    t5 = merge_sort(lst2)
    print("\nsorted_list:")
    print(f"bubble_sort:    list_size = {size} comparisons = {t1[0]} swaps = {t1[1]}    elapsed_time: {t1[2]:7f}")
    print(f"selection_sort: list_size = {size} comparisons = {t2[0]} swaps = {t2[1]}    elapsed_time: {t2[2]:7f}")
    print(f"insertion_sort: list_size = {size} comparisons = {t3[0]} swaps = {t3[1]}    elapsed_time: {t3[2]:7f}")
    print(f"quick_sort:     list_size = {size} comparisons = {t4[0]} swaps = {t4[1]}    elapsed_time: {t4[2]:7f}")
    print(f"merge_sort:     list_size = {size} comparisons = {t5[0]} swaps = {t5[1]}    elapsed_time: {t5[2]:7f}")

    lst3 = generate_reversed_list(size)
    t1 = bubble_sort(lst3)
    t2 = selection_sort(lst3)
    t3 = insertion_sort(lst3)
    t4 = quick_sort(lst3)
    t5 = merge_sort(lst3)
    print("\nreversed_list:")
    print(f"bubble_sort:    list_size = {size} comparisons = {t1[0]} swaps = {t1[1]}    elapsed_time: {t1[2]:7f}")
    print(f"selection_sort: list_size = {size} comparisons = {t2[0]} swaps = {t2[1]}    elapsed_time: {t2[2]:7f}")
    print(f"insertion_sort: list_size = {size} comparisons = {t3[0]} swaps = {t3[1]}    elapsed_time: {t3[2]:7f}")
    print(f"quick_sort:     list_size = {size} comparisons = {t4[0]} swaps = {t4[1]}    elapsed_time: {t4[2]:7f}")
    print(f"merge_sort:     list_size = {size} comparisons = {t5[0]} swaps = {t5[1]}    elapsed_time: {t5[2]:7f}")

    lst4 = generate_nearly_sorted_list(size)
    t1 = bubble_sort(lst4)
    t2 = selection_sort(lst4)
    t3 = insertion_sort(lst4)
    t4 = quick_sort(lst4)
    t5 = merge_sort(lst4)
    print("\nduplicate_list:")
    print(f"bubble_sort:    list_size = {size} comparisons = {t1[0]} swaps = {t1[1]}    elapsed_time: {t1[2]:7f}")
    print(f"selection_sort: list_size = {size} comparisons = {t2[0]} swaps = {t2[1]}    elapsed_time: {t2[2]:7f}")
    print(f"insertion_sort: list_size = {size} comparisons = {t3[0]} swaps = {t3[1]}    elapsed_time: {t3[2]:7f}")
    print(f"quick_sort:     list_size = {size} comparisons = {t4[0]} swaps = {t4[1]}    elapsed_time: {t4[2]:7f}")
    print(f"merge_sort:     list_size = {size} comparisons = {t5[0]} swaps = {t5[1]}    elapsed_time: {t5[2]:7f}")

    lst5 = generate_duplicate_list(size)
    t1 = bubble_sort(lst5)
    t2 = selection_sort(lst5)
    t3 = insertion_sort(lst5)
    t4 = quick_sort(lst5)
    t5 = merge_sort(lst5)
    print("\nduplicate_list:")
    print(f"bubble_sort:    list_size = {size} comparisons = {t1[0]} swaps = {t1[1]}    elapsed_time: {t1[2]:7f}")
    print(f"selection_sort: list_size = {size} comparisons = {t2[0]} swaps = {t2[1]}    elapsed_time: {t2[2]:7f}")
    print(f"quick_sort:     list_size = {size} comparisons = {t3[0]} swaps = {t3[1]}    elapsed_time: {t3[2]:7f}")
    print(f"insertion_sort: list_size = {size} comparisons = {t3[0]} swaps = {t3[1]}    elapsed_time: {t3[2]:7f}")
    print(f"quick_sort:     list_size = {size} comparisons = {t4[0]} swaps = {t4[1]}    elapsed_time: {t4[2]:7f}")
    print(f"merge_sort:     list_size = {size} comparisons = {t5[0]} swaps = {t5[1]}    elapsed_time: {t5[2]:7f}")


test(100)