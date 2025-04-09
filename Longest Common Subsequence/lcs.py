def find_lcs_length(X: str, Y: str):
    m = len(X)
    n = len(Y)

    # initializing a matrix of size (m+1, n+1)
    dp = [[0] * (n + 1) for x in range(m + 1)]

    # building dp[m+1][n+1] in bottom up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    
    return dp[m][n]

if __name__ == "__main__":
    X = "ABCBDAB"
    Y = "BDCABA"

    lcs_length = find_lcs_length(X, Y)
    print(f"LCS length: {lcs_length}")