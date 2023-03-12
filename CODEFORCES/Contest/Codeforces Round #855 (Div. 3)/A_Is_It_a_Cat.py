t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s = s.lower()
    sample = "meow"
    j = 0
    data = [s[0]]
    i = 1
    while i < n:
        while i < n and s[i] == s[i-1]:
            i += 1
        if i == n:
            break
        else:
            data.append(s[i])
        i += 1
    if data == ['m', 'e', 'o', 'w']:
        print("YES")
    else:
        print("NO")
