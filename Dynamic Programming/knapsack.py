from typing import List

global weights, values, W, F

weights = [ 2, 1, 3, 2 ]
values = [ 12, 10, 20, 15 ]
W, n = 5, len(weights)

# initialising the F-table for storing DP values
F = [[-1] * (W + 1) for i in range(n + 1)]

for i in range(n + 1):
    F[i][0] = 0

for j in range(W + 1):
    F[0][j] = 0

def mf_knapsack(i: int, j: int):
    if F[i][j] < 0:
        if j < weights[i]:
            value = mf_knapsack(i - 1, j)
        else:
            value = max(
                mf_knapsack(i - 1, j), 
                values[i] + mf_knapsack(i - 1, j - weights[i])
            )
        F[i][j] = value
    return F[i][j]

max_value = mf_knapsack(n - 1, W)
print(f"Maximum value: {max_value}")