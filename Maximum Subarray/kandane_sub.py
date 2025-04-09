def find_maximum_subarray(arr):
    start = temp_start = end = 0
    current_sum = max_sum = arr[0]

    for i in range(1, len(arr)):
        if current_sum + arr[i] > arr[i]:
            current_sum += arr[i]
        else:
            current_sum = arr[i]
            temp_start = i

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return start, end, max_sum

if __name__ == "__main__":
    import numpy as np
    np.random.seed(69)

    arr = list(np.random.randint(-100, 100, 10))
    start, end, max_sum = find_maximum_subarray(arr)

    print(f"Array: {arr}")
    print(f"Maximum Sum: {max_sum}")
    print(f"Subarray: {arr[start:end+1]}")