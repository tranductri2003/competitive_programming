t = int(input())
for _ in range(t):
    A, B, n = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n-1):
        time = b[i]//A
        if b[i] % A != 0:
            time += 1
        B -= time*a[i]

    if B <= 0:
        print("NO")
    else:
        while b[n-1] > 0:
            B -= a[n-1]
            b[n-1] -= A
            if B <= 0:
                break
        if B <= 0 and b[n-1] > 0:
            print("NO")
        else:
            print("YES")
