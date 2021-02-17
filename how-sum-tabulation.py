def howSum(targetSum, nums):
    dp = [None] * (targetSum + 1)
    dp[0] = []
    for i in range(targetSum + 1):
        if dp[i] is not None:
            for num in nums:
                if i + num <= targetSum:
                    dp[i + num] = [*dp[i], num]

    return dp[targetSum]


print(howSum(7, [2, 4, 9]))
print(howSum(8, [5, 4, 9]))
print(howSum(10, [2, 4, 9]))
print(howSum(25, [7, 4, 9]))