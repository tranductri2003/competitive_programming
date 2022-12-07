
t = int(input())
for _ in range(t):
    n = int(input())
    s = ""
    for i in range(n):
        s += "BAN"
    s = list(s)
    res = 0
    data = []
    for i in range(len(s)-1, -1, -1):
        if s[i] == "N":
            for j in range(0, i):
                if s[j] == "B":
                    s[i], s[j] = s[j], s[i]
                    res += 1
                    data.append((j+1, i+1))
                    break
    print(res)
    for num in data:
        print(num[0], num[1])
