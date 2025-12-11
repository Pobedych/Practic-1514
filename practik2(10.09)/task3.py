def permutations(sequence):
    elements = list(sequence)
    length = len(elements)
    if length == 0:
        return tuple()
    
    all_per = []
    elements.sort()
    all_per.append(tuple(elements))
    
    while True:
        pivot_index = length - 2
        while pivot_index >= 0 and elements[pivot_index] >= elements[pivot_index + 1]:
            pivot_index -= 1
        
        if pivot_index < 0:
            break
        
        si = length - 1
        while elements[si] <= elements[pivot_index]:
            si -= 1
        
        elements[pivot_index], elements[si] = elements[si], elements[pivot_index]
        
        start = pivot_index + 1
        end = length - 1
        while start < end:
            elements[start], elements[end] = elements[end], elements[start]
            start += 1
            end -= 1
        
        all_per.append(tuple(elements))
    
    return tuple(all_per)