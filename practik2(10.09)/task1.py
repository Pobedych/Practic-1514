def allsubsets(s):
    result = [tuple()]
    
    for elem in s:
        ns = []
        for subset in result:
            ns.append(subset + (elem,))
        result.extend(ns)
    
    return tuple(result)