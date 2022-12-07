t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    khac = True
    for i in range(n):
        if a[i] != b[i]:
            pass
        else:
            stop = False
            break
    if a == b:
        if a == b == '1'*n:
            print("YES")
            print(2)
            print(1, 1)
            print(2, n)
        elif a == b == '0'*n:
            print("YES")
            print(0)
        else:
            left = 0
            right = 0
            for i in range(0, n):
                if a[i] == '1':
                    left += 1
                else:
                    break
            for i in range(n-1, -1, -1):
                if a[i] == '1':
                    right += 1
                else:
                    break
            if left+right != a.count('1'):
                left0 = 0
                right0 = 0
                for i in range(0, n):
                    if a[i] == '0':
                        left0 += 1
                    else:
                        break
                for i in range(n-1, -1, -1):
                    if a[i] == '0':
                        right0 += 1
                    else:
                        break
                if left0+right0 != a.count('0'):
                    print("NO")
                else:
                    print("YES")
                    print(2)
                    print(1, n-right0)
                    print(1, left0)
            else:
                print("YES")
                if left == 0:
                    print(2)
                    print(1, n)
                    print(1, n-right)
                elif right == 0:
                    print(2)
                    print(1, n)
                    print(left+1, n)
                else:
                    print(2)
                    print(1, n)
                    print(left+1, n-right)
    elif khac == True:
        aa = list(a)
        for i in range(n):
            if aa[i] == '1':
                aa[i] = '0'
            else:
                aa[i] = '1'
        a = "".join(aa)
        if a == b == '1'*n:
            print("YES")
            print(3)
            print(1, n)
            print(1, 1)
            print(2, n)
        elif a == b == '0'*n:
            print("YES")
            print(1)
            print(1, n)
        else:
            left = 0
            right = 0
            for i in range(0, n):
                if a[i] == '1':
                    left += 1
                else:
                    break
            for i in range(n-1, -1, -1):
                if a[i] == '1':
                    right += 1
                else:
                    break
            if left+right != a.count('1'):
                left0 = 0
                right0 = 0
                for i in range(0, n):
                    if a[i] == '0':
                        left0 += 1
                    else:
                        break
                for i in range(n-1, -1, -1):
                    if a[i] == '0':
                        right0 += 1
                    else:
                        break
                if left0+right0 != a.count('0'):
                    print("NO")
                else:
                    print("YES")
                    print(3)
                    print(1, n)
                    print(1, n-right0)
                    print(1, left0)
            else:
                print("YES")
                if left == 0:
                    print(3)
                    print(1, n)
                    print(1, n)
                    print(1, n-right)
                elif right == 0:
                    print(3)
                    print(1, n)
                    print(1, n)
                    print(left+1, n)
                else:
                    print(3)
                    print(1, n)
                    print(1, n)
                    print(left+1, n-right)
    else:
        print("NO")
