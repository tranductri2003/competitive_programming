t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s = list(set(s))
    print(ord(max(s))-96)
