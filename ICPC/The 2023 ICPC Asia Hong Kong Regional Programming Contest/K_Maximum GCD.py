n = int(input())
a = list(map(int, input().split()))


def check(target):
    for x in a:
        if target == x or x % target == 0:
            pass
        else:
            if x % 2 == 0:
                if target < x//2:
                    pass
                else:
                    return False
            else:
                if target <= x//2:
                    pass
                else:
                    return False

    return True


res = min(a)
if check(res):
    print(res)
else:
    print(res//2)
