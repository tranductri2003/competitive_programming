from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print("No")
    else:
        print("Yes")
        data = [i for i in range(0, 2*n+1)]
        i = n
        j = n+1
        check = defaultdict(lambda: True)
        while j <= 2*n:
            print(i, j)
            check[i] = False
            check[j] = False
            i -= 1
            j += 2
        temp = []
        for k in range(n+1, 2*n+1):
            if check[k] == True:
                temp.append(k)
        j = 0
        for k in range(i, 0, -1):
            print(k, temp[j])
            j += 1
