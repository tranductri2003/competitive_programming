def check(s):
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            pass
        else:
            return False
    return True


test = int(input())
for _ in range(test):
    n, m = list(map(int, input().split()))
    s = input()
    t = input()

    if check(s) == check(t) == True:
        print("YES")
    else:
        res1 = False
        res2 = False

        for i in range(len(t)):
            if check(s+t[:-i]) and check(t[:i]):
                res1 = True
                break

        for i in range(len(s)):
            print('a')
            print(s[:i])
            print(t+s[:-i])
            if check(s[:i]) and check(t+s[:-i]):
                res2 = True
                break

        print(res1, res2)
        if res1 or res2:
            print("YES")
        else:
            print("NO")
