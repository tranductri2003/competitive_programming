
import sys
sys.stdin = open("sieve.in", "r")
for _ in range(int(input())):
    s1 = input()
    s2 = input()
    if s1+s2 != s2+s1:
        print(0)
    else:
        import math
        print(math.gcd(len(s1), len(s2)))
