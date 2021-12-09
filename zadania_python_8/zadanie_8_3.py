import random 

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    tmp = 0
    for i in range(0, n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)

        r = x*x + y*y
        if r <= 1:
            tmp += 1
    
    pi = (4 * tmp) / n
    return pi


print("PI : " + str(calc_pi(100)))
