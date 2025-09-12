def solve_rebus_optimized():
    solutions = []
    
    for Y in range(10):
        for K in range(10):
            for I in range(10):
                A = Y * K * I
                B = K * I
                
                right_part = A + Y + I
                
                if right_part == 0:
                    continue
                
                numerator = 577 * right_part - 520 * (B + 1)
                denominator = 520 * A
                
                if denominator != 0 and numerator % denominator == 0:
                    J = numerator // denominator
                    if 0 <= J <= 9:
                        solutions.append((J, Y, K, I))
                    
                elif A == 0:
                    if 520 * (B + 1) == 577 * (Y + I):
                        solutions.append((0, Y, K, I))
    
    return solutions

solutions = solve_rebus_optimized()

print(f"Ж = {solutions[0][0]}, У = {solutions[0][1]}, К = {solutions[0][2]}, И = {solutions[0][3]}")
        
      
