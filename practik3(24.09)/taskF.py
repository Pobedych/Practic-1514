n = int(input())

if n <= 0:
    result = []
else:
    fib_list = []
    a, b = 1, 1
    
    for i in range(n):
        fib_list.append((i + 1, a))
        a, b = b, a + b

    result = fib_list

print(' '.join(f"({x}, {y})" for x, y in result))
