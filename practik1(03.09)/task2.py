def sieve_of_eratosthenes(n):

    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False 
  
  
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]: 
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

n = int(input("Введите верхнюю границу: "))
primes = sieve_of_eratosthenes(n)
print(primes)