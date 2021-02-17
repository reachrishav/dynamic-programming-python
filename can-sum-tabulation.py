def canSum(targetSum, nums):
    dp = [False] * (targetSum + 1)
    dp[0] = True
    for i in range(targetSum + 1):
        if dp[i]:
            for num in nums:
                if i + num <= targetSum:
                    dp[i + num] = True

    return dp[targetSum]


print(canSum(7, [2, 4, 9]))
print(canSum(8, [5, 4, 9]))
print(canSum(10, [2, 4, 9]))
print(canSum(25, [7, 4, 9]))