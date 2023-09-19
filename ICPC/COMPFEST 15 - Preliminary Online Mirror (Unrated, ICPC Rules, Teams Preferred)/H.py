MOD = 998244353

def count_arrays(N, K):
    result = (K * pow(K + 1, N - 1, MOD)) % MOD
    return result

# Đọc input từ người dùng
N, K = map(int, input().split())

# Tính và in số cách sắp xếp
result = count_arrays(N, K)
print(result)
