def fact_generator():
    n = 1
    factorial = 1
    
    while True:
        yield factorial
        n += 1
        factorial *= n
