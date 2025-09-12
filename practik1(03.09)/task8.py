def find_longest_asc(arr):
    seqs, curr = [], []
    for i in range(len(arr)):
        curr = [arr[i]] if not curr or arr[i] <= arr[i-1] else curr + [arr[i]]
        seqs.append(curr)
    max_len = max(len(s) for s in seqs)
    return [s for s in seqs if len(s) == max_len]


numbers = [1, 2, 3, 1, 2, 4, 5, 1, 2, 3, 4]
print(find_longest_asc(numbers))