def calculate_pisano_period(p):
    if p == 2:
        return 3
    elif p == 5:
        return 20

    if p % 5 == 1 or p % 5 == 4:
        period = p - 1
    elif p % 5 == 2 or p % 5 == 3:
        period = 2 * p + 2

    return period

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_pisano_period_large(p):
    if p <= 1:
        return 0
    
    period = 1
    a, b = 1, 1

    while not (a == 1 and b == 0):
        a, b = b, (a + b) % p
        period += 1

    return period

p = int(input())

if p <= 5:
    result = calculate_pisano_period(p)
else:
    if p % 5 == 0:
        result = calculate_pisano_period_large(p)
    else:
        result = calculate_pisano_period(p)

print(result)
