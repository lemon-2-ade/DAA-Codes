from typing import List
import random

def partition(arr: List[int], low: int, high: int):
    pivot = arr[low]
    start, end = low, high

    while start < end:
        while start < end and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    
    arr[low] = arr[end]
    arr[end] = pivot

    return end

def randomized_partition(arr: List[int], low: int, high: int):
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return partition(arr, low, high)

def randomized_quicksort(arr: List[int], low: int, high: int):
    if (low < high):
        position = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, position - 1)
        randomized_quicksort(arr, position + 1, high)

def is_sorted(arr: List[int]):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

if __name__ == '__main__':
    arr = [random.randint(-100, 100) for i in range(20)]
    print(f"Original array: {arr}")
    
    randomized_quicksort(arr, 0, len(arr) - 1)
    print(f"Is sorted? {arr}")