t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print("NO")
    else:
        i = 0
        stop1 = False
        stop2 = False
        while i < n:
            if a[i] == 1:
                i += 2
            elif a[i] <= (n-i-1):
                i += a[i]+1
            else:
                if i == n-1:
                    stop1 = True
                    break
                else:
                    if a[i+1] == 1:
                        i += 2
                    else:
                        stop1 = True
                        break
        a = a[::-1]
        i = 0
        while i < n:
            if a[i] == 1:
                i += 2
            elif a[i] <= (n-i-1):
                i += a[i]+1
            else:
                if i == n-1:
                    stop2 = True
                    break
                else:
                    if a[i+1] == 1:
                        i += 2
                    else:
                        stop2 = True
                        break
        if stop1 == stop2 == True:
            print("NO")
        else:
            print("YES")
