n = int(input())
while True:
    for i in range(1, n):
        print(i, i+1)
        s = input()
        if s == "WIN":
            quit()
    for i in range(n-1, 0, -1):
        print(i, i+1)
        s = input()
        if s == "WIN":
            quit()
