from typing import List
import random, time

def partition(arr: List[int], low: int, high: int):
    """partitions the array around the pivot (initially arr[low])."""
    pivot = arr[low]
    start = low + 1
    end = high

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
    """chooses a random pivot and partitions the array."""
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

    return partition(arr, low, high)

def randomized_qsort(arr: List[int], low: int, high: int):
    if low < high:
        position = randomized_partition(arr, low, high)
        randomized_qsort(arr, low, position - 1)
        randomized_qsort(arr, position + 1, high)

if __name__ == "__main__":
    
    random.seed(69)
    start_time = time.time()

    arr = [random.randint(-999, 999) for i in range(1000000)]
    print(f"Original array: {arr}")

    end_time = time.time()
    print(f"Time elapsed: {end_time - start_time:.2f}")
    start_time = time.time()

    randomized_qsort(arr, 0, len(arr) - 1)
    print(f"\nSorted array: {arr}")

    end_time = time.time()
    print(f"Time elapsed: {end_time - start_time:.2f}")