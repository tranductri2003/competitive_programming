def check(left, right, pos, s):
    if left == right:
        return True
    if s[pos] == "=":
        return False
    if s[pos] == "<":
        mid = (left+right+1)//2
        return check(left, mid-1, pos+1, s)
    if s[pos] == ">":
        mid = (left+right-1)//2
        return check(mid+1, right, pos+1, s)


def solve(left, right, pos, s):
    if s[pos] == "=":
        print(left)
        return
    if s[pos] == "<" and check(left, right-1, pos+1, s) == True:
        print(right, end=" ")
        solve(left, right-1, pos+1, s)
        return
    if s[pos] == ">" and check(left+1, right, pos+1, s) == True:
        print(left, end=" ")
        solve(left+1, right, pos+1, s)
        return
    if s[pos] == "<":
        mid = (left+right+1)//2
        print(mid, end=" ")
        solve(left, mid-1, pos+1, s)
        return
    if s[pos] == ">":
        mid = (left+right-1)//2
        print(mid, end=" ")
        solve(mid+1, right, pos+1, s)
        return


stop = 0
N, K = list(map(int, input().split()))
s = input()
length = len(s)
if s[length-1] == "=" and length > N:
    print(-1)
    stop = 1
else:
    if s[length-1] != "=" and length >= N:
        print(-1)
        stop = 1

if stop == 0:

    if s[length-1] != "=":
        left = 1
        right = N
        for i in range(length):
            if s[i] == "<":
                print(right, end=" ")
                right -= 1
            if s[i] == ">":
                print(left, end=" ")
                left += 1
                stop = 1

if stop == 0:
    if check(1, N, 0, s) == False:
        print(-1)
        stop = 1

if stop == 0:
    solve(1, N, 0, s)
