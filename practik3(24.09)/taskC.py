list1 = set(map(int, input().split()))
list2 = set(map(int, input().split()))

result = sorted(list1 ^ list2)

for num in result:
    print(num)
