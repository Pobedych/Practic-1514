import random

arr = [random.randint(0, 1) for _ in range(10)]
print("Список:", arr)
s = ''.join(map(str, arr))
max_seq = max(s.split('0'), key=len)
start = s.find(max_seq)
end = start + len(max_seq) - 1
print(f"Индексы: {start}-{end}")