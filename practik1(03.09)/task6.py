def syracuse(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

for i in range(1, 1001):
    steps = syracuse(i)
    print(f"{i}: достигло 1 за {steps} шагов")

print("Гипотеза верна для первых 1000 чисел!")