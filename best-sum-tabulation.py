def bestSum(targetSum, nums):
    dp = [None] * (targetSum + 1)
    dp[0] = []
    for i in range(targetSum + 1):
        if dp[i] is not None:
            for num in nums:
                if i + num <= targetSum:
                    newCombination = [*dp[i], num]
                    if not dp[i + num] or len(newCombination) < len(
                            dp[i + num]):
                        dp[i + num] = newCombination

    return dp[targetSum]


print(bestSum(7, [2, 4, 9]))
print(bestSum(8, [5, 4, 9]))
print(bestSum(90, [2, 4, 9]))
print(bestSum(100, [7, 4, 9]))