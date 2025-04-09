from typing import List

def get_longest_bitonic_subarray(arr: List[int], n: int):

    if n == 0:
        return 0, []
    
    inc = [1] * n
    dec = [1] * n

    # increasing order
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            inc[i] = inc[i - 1] + 1
    
    # decreasing order
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            dec[i] = dec[i + 1] + 1

    max_len = peak_index = 0

    for i in range(n):
        bitonic_len = inc[i] + dec[i] - 1

        if bitonic_len > max_len:
            max_len = bitonic_len
            peak_index = i

    # reconstructing the bitonic subarray
    start = peak_index - (inc[peak_index] - 1)
    end = peak_index + (inc[peak_index] - 1)
    bitonic_subarray = arr[start : end + 1]

    return bitonic_len, bitonic_subarray
    

if __name__ == "__main__":

    n = int(input("Enter the length of the array: "))
    print("Enter the array: ", end="")
    arr = list(map(int, input().split()))

    bitonic_len, bitonic_arr = get_longest_bitonic_subarray(arr, n)

    print(f"Bitonic subarray length: {bitonic_len}")
    print(f"Bitonic subarray: {bitonic_arr}")