sample = "3141592653589793238462643383279"


t = int(input())
for _ in range(t):
    s = input()
    res = 0
    for i in range(len(s)):
        if s[i] == sample[i]:
            res += 1
        else:
            break
    print(res)
