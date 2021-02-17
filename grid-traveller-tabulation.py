def gridTraveller(m, n):
    dp = [[0] * (n + 2) for _ in range(m + 2)]
    dp[1][1] = 1

    for i in range(m + 1):
        for j in range(n + 1):
            dp[i][j + 1] += dp[i][j]
            dp[i + 1][j] += dp[i][j]

    return dp[m][n]


print(gridTraveller(3, 3))
print(gridTraveller(5, 6))
print(gridTraveller(18, 18))
