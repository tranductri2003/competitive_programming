from collections import defaultdict


def uoc(n):
    i = 1
    data = []
    while i*i <= n:
        if i*i == n:
            data.append(i)
        else:
            if n % i == 0:
                data.append(i)
                data.append(n//i)
        i += 1

    return data


t = int(input())
for _ in range(t):
    n = int(input())
    data = uoc(n)
    data.sort()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    data = uoc(n)
    check = defaultdict(lambda: False)
    for num in data:
        check[num] = True

    for i in range(1, n+1):
        if check[i] == False:
            temp = i
            break
    else:
        temp = n+1
    res = ""
    for i in range(n):
        res += alphabet[i % temp]

    print(res)
