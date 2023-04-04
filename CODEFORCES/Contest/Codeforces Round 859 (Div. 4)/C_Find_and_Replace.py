from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    check = defaultdict(list)
    for i in range(len(alphabet)):
        for j in range(n):
            if s[j] == alphabet[i]:
                check[alphabet[i]].append(j)

    stop = False
    for i in range(len(alphabet)):
        data = check[alphabet[i]]
        for j in range(1, len(data)):
            if data[j] % 2 != data[j-1] % 2:
                stop = True
    if stop == False:
        print("YES")
    else:
        print("NO")
