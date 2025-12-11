def kelemsubsets(s, k):
    def generate_subsets(start, current):
        if len(current) == k:
            result.append(tuple(current))
            return
        
        for i in range(start, len(s)):
            current.append(s[i])
            generate_subsets(i + 1, current)
            current.pop()
    
    if k < 0 or k > len(s):
        return ()
    if k == 0:
        return ((),)
    
    result = []
    generate_subsets(0, [])
    return tuple(result)