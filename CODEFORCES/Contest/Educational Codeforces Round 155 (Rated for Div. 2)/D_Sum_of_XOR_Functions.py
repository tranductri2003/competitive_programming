MOD = 998244353

def calculate_xor_sum(n, a):
    prefix_xor = [0] * (n + 1)
    for i in range(n):
        prefix_xor[i + 1] = prefix_xor[i] ^ a[i]

    result = 0
    for l in range(n):
        xor_sum = 0
        for r in range(l, n):
            xor_sum ^= a[r]
            result += (r - l + 1) * xor_sum
            result %= MOD

    return result

n = int(input())
a = list(map(int, input().split()))
result = calculate_xor_sum(n, a)
print(result)
