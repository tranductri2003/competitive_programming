
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    i = 0
    time = 0
    status = True
    while i < n:
        if time % 2 == 0:
            i += 1
            time += 1
        else:
            if i+1 >= n:
                status = False
                break
            if s[i+1] != s[i]:
                status = False
                break
            i += 2
            time += 1
    if status == True:
        print("YES")
    else:
        print("NO")
