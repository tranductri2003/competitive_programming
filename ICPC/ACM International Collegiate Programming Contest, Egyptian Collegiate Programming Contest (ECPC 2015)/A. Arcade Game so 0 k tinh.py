import math
for _ in range(int(input())):
    s = input()
    n = len(s)
    existingNumber = list(s)

    if list(s) == sorted(s, reverse=True):
        res = 0
    else:
        pos = 1
        res = 0
        # Tim vi tri cua hoan vi
        for i in range(n):
            used = list(s[:i+1])
            possible = 0
            for num in existingNumber:
                if num not in used and num < s[i]:
                    possible += 1
            pos += possible*math.factorial(n-i-1)
        p = 1/(math.factorial(n))
        soOGiua = max(0, math.factorial(n)-pos-1)
        res = p*((p+1)**(soOGiua))
    res = format(res, ".9f")
    print(res)
