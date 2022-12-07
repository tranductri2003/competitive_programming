
for _ in range(int(input())):
    n = int(input())
    t = input()
    s = ""
    data = []
    i = len(t)-1
    while True:
        if i < 0:
            break
        if t[i] != '0':
            data.append(int(t[i]))
            i -= 1
        else:
            temp = int(t[i-2]+t[i-1])
            data.append(temp)
            i = i-3
    data = data[::-1]
    for num in data:
        s += chr(num+96)
    print(s)
