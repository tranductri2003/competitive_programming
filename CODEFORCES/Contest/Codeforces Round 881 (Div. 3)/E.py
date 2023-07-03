from collections import defaultdict
s = input()
check = defaultdict(lambda: 0)
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(s)):
    check[s[i]] += 1

res = 0
tich = 1

for i in range(len(alphabet)):
    tich *= 2**check[alphabet[i]]

for i in range(len(alphabet)):
    socachlaysai = (2**(check[alphabet[i]])-(1+check[alphabet[i]]))
    print(socachlaysai)
print(res)
print(2**(len(s))-res)
