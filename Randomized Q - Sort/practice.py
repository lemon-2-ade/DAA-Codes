from typing import List
import random

def partition(arr: List[int], low: int, high: int):

    pivot = arr[low]
    start, end = low + 1, high

    while True:
        while start <= end and arr[start] <= pivot:
            start += 1
        
        while end >= start and arr[end] > pivot:
            end -= 1
        
        if start > end:
            break
        else:
            arr[start], arr[end] = arr[end], arr[start]
    
    arr[low], arr[end] = arr[end], arr[low]

    return end

def randomized_partition(arr: List[int], low: int, high: int):

    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

    return partition(arr, low, high)

def randomized_qsort(arr: List[int], low: int, high: 0):
    if low < high:
        position = randomized_partition(arr, low, high)
        randomized_qsort(arr, low, position - 1)
        randomized_qsort(arr, position + 1, high)

if __name__ == "__main__":
    random.seed(69)

    arr = [random.randint(-100, 100) for i in range(10)]
    print(f"Original array: {arr}")

    randomized_qsort(arr, 0, len(arr) - 1)
    print(f"Sorted array: {arr}")