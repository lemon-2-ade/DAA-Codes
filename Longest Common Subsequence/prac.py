def get_lcs(x: str, y: str):
    n, m = len(x), len(y)
    dp = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    index = dp[n][m]
    lcs = [ None ] * index
    i, j = n, m

    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            lcs[index - 1] = x[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcs = ''.join(lcs)
    lcs_length = dp[n][m]

    return lcs, lcs_length
    
if __name__ == '__main__':

    x = 'ACCGGTCGAGTGCGCGGAAGCCGGCCGAA'
    y = 'GTCGTTCGGAATGCCGTTGCTCTGTAAA'

    lcs, lcs_length = get_lcs(x, y)