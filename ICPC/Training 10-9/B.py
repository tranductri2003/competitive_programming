import math

def count_ways(n, k, p):
    num_ways = 0
    num_ways = math.comb(n + p - 1, n) - math.comb(n + p - 1 - k, n)
    return num_ways 


n, k, p = map(int, input().split())

ways = count_ways(n, k, p)
print(ways)
