from functools import lru_cache


@lru_cache
def recursion(i, j):
    if s[i][j] == "W":
        return False
    if s[i][j] == "B" and j == 0:
        return True
    if s[1-i][j] == "B":
        if recursion(1-i, j-1) == True or recursion(i, j-1) == True:
            return True
        else:
            return False
    else:
        return recursion(i, j-1)


t = int(input())
for _ in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    s = []
    for i in range(2):
        s.append([])
        for j in range(n):
            if i == 0:
                s[i].append(s1[j])
            else:
                s[i].append(s2[j])
    for i in range(2):
        print(*s[i])
    if n == 1:
        print("YES")
    else:
        check1 = False
        check2 = False

        for j in range(0, n-1):
            if s[0][j] == "B" and s[1][j+1] == "B" and s[1][j] == "W" and s[0][j+1] == "W":
                check1 = True
                break
            if s[0][j] == "W" and s[1][j+1] == "W" and s[1][j] == "B" and s[0][j+1] == "B":
                check1 = True
                break

        for j in range(1, n-1):
            if s[0][j-1] == "W" and s[0][j] == "B" and s[0][j+1] == "W" and s[1][j-1] == "B" and s[1][j] == "B" and s[1][j+1] == "B":
                check2 = True
            if s[0][j-1] == "B" and s[0][j] == "B" and s[0][j+1] == "B" and s[1][j-1] == "W" and s[1][j] == "B" and s[1][j+1] == "W":
                check2 = True
        if check1 == False and check2 == False:
            print("YES")
        else:
            print("NO")
