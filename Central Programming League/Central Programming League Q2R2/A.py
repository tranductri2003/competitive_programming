
from itertools import compress


def rwh_primes1v1(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


data = rwh_primes1v1(100)
l = 0
r = len(data)-1

while l < r:
    mid = (l+r+1)//2
    print("?", data[mid])
    a = input()
    if a == ">":
        r = mid-1
    else:
        l = mid
    if l == r:
        break
print(f"! {data[l]}")
