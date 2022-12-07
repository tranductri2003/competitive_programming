from collections import defaultdict
n, w, h, ss = list(map(int, input().split()))


data = defaultdict(lambda: 0)

current = 0
for i in range(n):
    c = input()
    temp = 0
    current = 0
    for time in range(h):
        s = input()+'.'
        if s[0] == "#":
            temp = 1
        else:
            temp = 0
        for j in range(1, w+1):
            if s[j] != s[j-1]:
                temp += 1
        current = max(current, temp)

    data[c] = current

temp = max(data.values())
char = ""
for num in data:
    if data[num] == temp:
        char = num
        break


if ss % data[char] == 0:
    print(char*(ss//data[char]))
else:
    print(char*(1+ss//data[char]))
