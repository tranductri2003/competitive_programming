import math

N = 100000
isPrime = [False] * (N + 5)
prime = []

def solve():
    n = int(input())
    m = n
    odd = []
    for i in prime:
        if m % i == 0:
            cnt = 0
            while m % i == 0:
                cnt += 1
                m //= i
            if cnt % 2 == 1:
                odd.append(i)
    if m != 1:
        odd.append(m)
    t = 1
    for x in odd:
        t *= x
    a = n // t
    b = int(math.sqrt(a)) + 1
    print(b * b * t - n)

if __name__ == "__main__":
    for i in range(2, int(math.sqrt(N)) + 1):
        if not isPrime[i]:
            for j in range(i * i, N + 1, i):
                isPrime[j] = True
    for i in range(2, N + 1):
        if not isPrime[i]:
            prime.append(i)
    # for i in range(10):
    #     print(prime[i], end=' ')
    test = 1
    # test = int(input())
    while test > 0:
        solve()
        test -= 1
