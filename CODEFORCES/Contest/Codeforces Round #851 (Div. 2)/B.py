def check(n):
    res = 0
    for i in range(len(str(n))):
        res += int(str(n)[i])
    return res


t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print(n//2, n//2)
    else:
        down = n//2
        up = n//2+1

        temp1 = check(down)
        temp2 = check(up)

        if temp1+1 == temp2 or temp1-1 == temp2 or temp1 == temp2:
            print(down, up)
        else:
            res1 = []
            res2 = []

            left = True
            for i in range(len(str(n))-1, -1, -1):
                if int(str(n)[i]) % 2 == 0:
                    res1.insert(0, int(str(n)[i])//2)
                    res2.insert(0, int(str(n)[i])//2)
                else:
                    if left == True:
                        res1.insert(0, int(str(n)[i])//2+1)
                        res2.insert(0, int(str(n)[i])//2)
                        left = False
                    else:
                        res1.insert(0, int(str(n)[i])//2)
                        res2.insert(0, int(str(n)[i])//2+1)
                        left = True
            ans1 = ""
            ans2 = ""
            for num in res1:
                ans1 += str(num)
            for num in res2:
                ans2 += str(num)
            print(int(ans1), int(ans2))
