def canConstruct(target, wordBank):
    targetLength = len(target)
    dp = [[] for _ in range(targetLength + 1)]
    dp[0] = [[]]

    for i in range(targetLength + 1):
        for word in wordBank:
            if target[i:i + len(word)] == word:
                newCombination = [[*subArray, word] for subArray in dp[i]]
                dp[i + len(word)] += [*newCombination]

    return dp[targetLength]


print(canConstruct('abcdef', ['ab', 'c', 'def']))
print(canConstruct('rishav', ['rish', 'h', 'hav']))
print(canConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl', 'e']))
print(canConstruct('rishav', ['r', 'ish', 'av', 'is', 'hav']))