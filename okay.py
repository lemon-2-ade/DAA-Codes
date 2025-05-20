from typing import List, Tuple

global numbers, n
path, subsets = [], []

def backtrack(index: int):
    if index == n:
        subsets.append(path.copy())
        return

    next_number = numbers[index]
    backtrack(next_number)      # not using the number
    path.append(next_number)
    backtrack(index + 1)
    path.pop()

if __name__ == '__main__': 
    print("Enter the list of numbers: ")
    numbers = list(map(int, input().split()))
    n = len(numbers)

    backtrack(0)
    print(f"Subsets obtained: {subsets}")