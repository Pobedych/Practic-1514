import math

def factorize_optimized(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
 
    divisor = 3
    max_divisor = math.isqrt(n) 
    
    while divisor <= max_divisor and n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
            max_divisor = math.isqrt(n)
        divisor += 2 
    
    if n > 1:
        factors.append(n)
    
    return factors

number = int(input())
factors = factorize_optimized(number)

print(" ".join(map(str, factors)))