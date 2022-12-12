from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if n == 1:
        print("NO")
    else:
        stop = False
        check = defaultdict(lambda: 0)
        for i in range(0, n-1):
            temp = s[i]+s[i+1]
            if check[temp] >= 2 or (check[temp] == 1 and ((s[i-1]+s[i]) != (s[i]+s[i+1]))):
                print("YES")
                stop = True
                break
            else:
                check[temp] += 1
        if stop == False:
            print("NO")
