def LIST_BEGIN(L):
    """Возвращает начало непустого списка (все элементы кроме последнего)"""
    return L[:-1]

def LIST_LEN(L):
    """Подсчитывает длину списка"""
    return len(L)

def LIST_REVERSE(L):
    """Переворачивает список"""
    return L[::-1]

def COUNT_ATOMS(L):
    """Подсчитывает количество атомов в списке (элементов, которые не являются списками)"""
    count = 0
    for item in L:
        if not isinstance(item, list):
            count += 1
    return count

def ONLY_ATOMS(L):
    """Получает новый список только из атомов данного"""
    return [item for item in L if not isinstance(item, list)]

def INTO_SORT(element, L):
    """Добавляет элемент в упорядоченный список, не нарушая упорядоченности"""
    result = L[:]
    inserted = False
    for i in range(len(result)):
        if element <= result[i]:
            result.insert(i, element)
            inserted = True
            break
    if not inserted:
        result.append(element)
    return result

def LIST_SORT(L):
    """Сортирует список"""
    return sorted(L)

def LISTS_MERGE(L, R):
    """Осуществляет слияние двух упорядоченных списков в один, также упорядоченный"""
    result = []
    i, j = 0, 0
    
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
    
    result.extend(L[i:])
    result.extend(R[j:])
    
    return result

def LIST_MAX(L):
    """Возвращает максимум непустого списка"""
    return max(L)

def LIST_MIN(L):
    """Возвращает минимум непустого списка"""
    return min(L)

def LIST_SUM(L):
    """Возвращает сумму всех элементов списка"""
    return sum(L)

def LIST_REMOVE(e, L):
    """Удаляет все элементы e из списка L"""
    return [item for item in L if item != e]

def ISSET(L):
    """Проверяет, является ли список L множеством (все элементы уникальны)"""
    return len(L) == len(set(L))

def INTO_SET(L):
    """Превращает список L в множество (удаляет дубликаты)"""
    result = []
    seen = set()
    for item in L:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

def IS_SUBSET(L, R):
    """Проверяет, является ли список L подмножеством R"""
    return set(L).issubset(set(R))

def EQ_SET(L, R):
    """Проверяет множества на равенство"""
    return set(L) == set(R)

def LIST_UNION(L, R):
    """Возвращает объединение двух списков-множеств"""
    result = L[:]
    for item in R:
        if item not in result:
            result.append(item)
    return result

def LIST_CROSS(L, R):
    """Возвращает пересечение двух списков-множеств"""
    return [item for item in L if item in R]

def LIST_ONION(N):
    """Возвращает список вложенности N"""
    if N == 0:
        return []
    result = []
    current = result
    for i in range(N - 1):
        current.append([])
        current = current[0]
    return result
