def rec_permutations(s):
    if len(s) == 0:
        return ((),)
    if len(s) == 1:
        return ((s[0],),)
    
    result = []
    
    for i in range(len(s)):
        current = s[i]
        remaining = s[:i] + s[i+1:]
        
        for perm in rec_permutations(remaining):
            result.append((current,) + perm)
    
    return tuple(result)