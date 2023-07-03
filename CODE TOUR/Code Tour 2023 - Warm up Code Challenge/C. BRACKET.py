n, k = list(map(int, input().split()))
# if n % 2 == 1:
binary = bin(k-1)[2:]
binary = '0'*(n-len(binary))+binary
res = ""
for i in range(len(binary)):
    if binary[i] == "0":
        res += "("
    else:
        res += ")"
print(res)
