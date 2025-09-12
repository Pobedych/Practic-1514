def soe(n):
    if n < 2:
        return []
    
    sim = [True] * (n + 1)
    sim[0] = sim[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if sim[i]:
            for j in range(i*i, n + 1, i):
                sim[j] = False
    
    return [i for i, is_prime in enumerate(sim) if is_prime]

A = int(input("начало диапазона "))
B = int(input("конец диапазона "))

all_primes = soe(B)
primes_in_range = [p for p in all_primes if p >= A]

with open("primes_number.txt", "w", encoding="utf-8") as file:
    if primes_in_range:
        for prime in primes_in_range:
            file.write(f"{str(prime)}\n")
        file.write(f"Длина: {str(len(primes_in_range))}")
    else:
        file.write("нет простых чисел")
