def canConstruct(target, wordBank):
    targetLength = len(target)
    dp = [False] * (targetLength + 1)
    dp[0] = True

    for i in range(targetLength + 1):
        if dp[i]:
            for word in wordBank:
                if target[i:i + len(word)] == word:
                    dp[i + len(word)] = True

    return dp[targetLength]


print(canConstruct('abcdef', ['ab', 'c', 'def']))
print(canConstruct('rishav', ['rish', 'h', 'hav']))
print(canConstruct('rishav', ['r', 'ish', 'av']))
