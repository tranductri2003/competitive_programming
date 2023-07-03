from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    check = defaultdict(lambda: 0)
    for chu in s:
        check[chu] += 1

    stop = False

    if n % 2 == 0:
        for chu in alphabet:
            if check[chu] > n//2:
                stop = True
                break

    if n % 2 == 1 or stop == True:
        print(-1)
    else:
        print("Chua biet")
