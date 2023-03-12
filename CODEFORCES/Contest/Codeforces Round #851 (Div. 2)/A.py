t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    num2 = a.count(2)
    if num2 % 2 == 1:
        print(-1)
    elif num2 == 0:
        print(1)
    else:
        pos = num2//2
        temp = 0
        for i in range(n):
            if a[i] == 2:
                temp += 1
                if temp == pos:
                    print(i+1)
                    break
