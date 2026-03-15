def rec_permutations(s):
    
    result = []
    for i in range(len(s)):
        current = s[i]
        remaining = s[:i] + s[i+1:]
        for perm in rec_permutations(remaining):
            result.append((current,) + perm)
    
    return tuple(result)