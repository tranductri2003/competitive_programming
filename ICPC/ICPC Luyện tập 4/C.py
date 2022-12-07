def choose(s, l, r):
    if r-l <= 2:
        return 0
    else:
        if s[l+1] < s[r-1]:
            return 1
        elif s[l+1] > s[r-1]:
            return -1
        else:
            return choose(s, l+1, r-1)


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
    elif s[r] < s[l]:
        res += s[r]
        r -= 1
    else:

        if choose(s, l, r) == 0:
            res += s[r]
            r -= 1
        elif choose(s, l, r) == 1:
            res += s[l]
            l += 1
        else:
            res += s[r]
            r -= 1

print(res)
