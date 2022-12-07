

n = int(input())
s = input()
res = ""
l = 0
r = n-1
while l <= r:
    if l == r:
        res += s[l]
        break
    if s[l] < s[r]:
        res += s[l]
        l += 1
    else:
        res += s[r]
        r -= 1
print(res)
