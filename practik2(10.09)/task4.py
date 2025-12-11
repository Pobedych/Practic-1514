def rec_permutations(s):
    # Базовый случай: если длина <= 1
    if len(s) <= 1:
        return (tuple(s),)
    
    result = []
    for i in range(len(s)):
        current = s[i]
        remaining = s[:i] + s[i+1:]
        for perm in rec_permutations(remaining):
            result.append((current,) + perm)
    
    return tuple(result)