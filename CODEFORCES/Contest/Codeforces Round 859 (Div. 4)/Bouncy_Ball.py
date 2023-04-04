def hitUp(i, j, n, m):
    if i == 1:
        return True
    else:
        return False


def hitDown(i, j, n, m):
    if i == n:
        return True
    else:
        return False


def hitLeft(i, j, n, m):
    if j == 1:
        return True
    else:
        return False


def hitRight(i, j, n, m):
    if j == m:
        return True
    else:
        return False


def hitLUCorner(i, j, n, m):
    if i == 1 and j == 1:
        return True
    else:
        return False


def hitRUCorner(i, j, n, m):
    if i == 1 and j == m:
        return True
    else:
        return False


def hitLDCorner(i, j, n, m):
    if i == n and j == 1:
        return True
    else:
        return False


def hitRDCorner(i, j, n, m):
    if i == n and j == m:
        return True
    else:
        return False


t = int(input())
for _ in range(t):
    n, m, i1, j1, i2, j2, direction = input().split()
    n = int(n)
    m = int(m)
    i1 = int(i1)
    j1 = int(j1)
    i2 = int(i2)
    j2 = int(j2)

    limitBound = 2*((n+1)//2+(m+1)//2)
    currentPosition = direction
    bounce = 0

    if i1 == i2 and j1 == j2:
        print(0)
    else:
        while True:
            if hitDown(i1, j1, n, m) or hitUp(i1, j1, n, m) or hitLeft(i1, j1, n, m) or hitRight(i1, j1, n, m) or hitLDCorner(i1, j1, n, m) or hitLUCorner(i1, j1, n, m) or hitRDCorner(i1, j1, n, m) or hitRUCorner(i1, j1, n, m):
                if hitRUCorner(i1, j1, n, m) or hitRDCorner(i1, j1, n, m) or hitLUCorner(i1, j1, n, m) or hitLDCorner(i1, j1, n, m):
                    if hitRUCorner(i1, j1, n, m):
                        currentPosition = "DL"
                        if i2-i1 == j1-j2:
                            break
                        temp = min(n, m)
                        i1 -= temp
                        j1 -= temp
                    elif hitRDCorner(i1, j1, n, m):
                        currentPosition = "UL"

                else:
                    if hitDown(i1, j1, n, m):
                        if currentPosition == "DL":
                            currentPosition = "UL"
                            if i1-i2 == j1-j2:
                                break
                            temp = min(i1, j1)
                            i1 -= temp
                            j1 -= temp
                        elif currentPosition == "DR":
                            currentPosition = "UR"
                            if i1-i2 == j2-j1:
                                break
                            temp = min(i1, m-j1)
                            i1 -= temp
                            j1 += temp
                    elif hitUp(i1, j1, n, m):
                        if currentPosition == "UL":
                            currentPosition = "DL"
                            if i2-i1 == j1-j2:
                                break
                            temp = min(j1, n)
                            i1 += temp
                            j1 -= temp
                        elif currentPosition == "UR":
                            currentPosition = "DR"
                            if i2-i1 == j2-j1:
                                break
                            temp = min(n, m-j1)
                            i1 += temp
                            j1 += temp
                    elif hitLeft(i1, j1, n, m):
                        if currentPosition == "DL":
                            currentPosition = "DR"
                            if i2-i1 == j2-j1:
                                break
                            temp = min(n-i1, m)
                            i1 += temp
                            j1 += temp
                        elif currentPosition == "UL":
                            currentPosition = "UR"
                            if i1-i2 == j2-j1:
                                break
                            temp = min(i1, m)
                            i1 -= temp
                            j1 += temp
                    else:
                        if currentPosition == "DR":
                            currentPosition = "DL"
                            if i2-i1 == j1-j2:
                                break
                            temp = min(m, n-i1)
                            i1 += temp
                            j1 -= temp
                        else:
                            currentPosition = "UL"
                            if i1-i2 == j1-j2:
                                break
                            temp = min(m, i1)
                            i1 -= temp
                            j1 -= temp
            print(i1, j1)
            a = input()

        if bounce == limitBound:
            print(-1)
        else:
            print(bounce)
