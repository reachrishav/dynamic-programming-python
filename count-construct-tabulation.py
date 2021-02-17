def canConstruct(target, wordBank):
    targetLength = len(target)
    dp = [0] * (targetLength + 1)
    dp[0] = 1

    for i in range(targetLength + 1):
        if dp[i]:
            for word in wordBank:
                if target[i:i + len(word)] == word:
                    dp[i + len(word)] += dp[i]

    return dp[targetLength]


print(canConstruct('abcdef', ['ab', 'c', 'def']))
print(canConstruct('rishav', ['rish', 'h', 'hav']))
print(canConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl', 'e']))
print(canConstruct('rishav', ['r', 'ish', 'av', 'is', 'hav']))
