from collections import defaultdict
s = input()

count = defaultdict(lambda: 0)
for i in range(len(s)):
    count[s[i]] += 1

res = 1
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alphabet)):
    res *= (count[alphabet[i]]+1)
print(res % 11092019)
