from typing import List
global N

def subset_sum(arr: List[int], total: int):
    subsets = []
    path = []

    def backtrack(index: int, current: int):
        if current == total:
            subsets.append(path[:])
            return

        if current > total or index >= N:
            return
        
        for i in range(index, N):
            path.append(arr[i])
            backtrack(i + 1, current + arr[i])
            path.pop()

    backtrack(0, 0)
    return subsets