
t = int(input())
for _ in range(t):
    s = input()
    res = []
    for i in range(len(s)):
        res.insert(0, s[i])
        res.append(s[i])
    res = "".join(res)
    print(res)
