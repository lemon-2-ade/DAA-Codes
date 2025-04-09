def find_maximum_subarray(arr, low, high):
    if high == low:
        return low, high, arr[low]
    
    mid = (low + high) // 2
    left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)
    right_low, right_high, right_sum = find_maximum_subarray(arr, mid+1, high)
    cross_low, cross_high, cross_sum = find_max_cross_subarray(arr, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum

def find_max_cross_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    max_left = mid
    summ = 0

    for i in range(mid, low-1, -1):
        summ += arr[i]
        if summ > left_sum:
            left_sum = summ
            max_left = i

    right_sum = float('-inf')
    max_right = mid + 1
    summ = 0

    for i in range(mid+1, high+1):
        summ += arr[i]
        if summ > right_sum:
            right_sum = summ
            max_right = i

    return max_left, max_right, left_sum + right_sum

if __name__ == "__main__":
    import numpy as np
    np.random.seed(69)

    # numbers = list(np.random.randint(-100, 100, 5))
    numbers = [-2, 3, 1, 4, -1, 3, 5, -4, 6, 1]
    left, right, max_sum = find_maximum_subarray(numbers, 0, len(numbers)-1)

    print(f"Array: {numbers}")
    print(f"Maximum sum: {max_sum}")
    print(f"Indices: {[left, right]}")