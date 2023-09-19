# Initialize the sea grid
s = [list(input()) for _ in range(10)]

# Initialize the ship grid and a dictionary to track ship counts
ship = [[0] * 10 for _ in range(10)]
mp = {}

# Check for a ship of size 4
ship4 = False
for i in range(10):
    for j in range(10):
        if s[i][j] == '#' and not ship[i][j]:
            cnt = 1
            for k in range(j + 1, j + 4):
                if 0 <= k < 10 and s[i][k] == '#' and not ship[i][k]:
                    cnt += 1
            if cnt == 4:
                ship4 = True
                for k in range(j, j + 4):
                    ship[i][k] = 1
                    mp[1] = 4
if not ship4:
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#' and not ship[i][j]:
                cnt = 1
                for k in range(i + 1, i + 4):
                    if 0 <= k < 10 and s[k][j] == '#' and not ship[k][j]:
                        cnt += 1
                if cnt == 4:
                    for k in range(i, i + 4):
                        ship[k][j] = 1
                        mp[1] = 4

# Check for two ships of size 3
ship3 = 0
for i in range(10):
    for j in range(10):
        if s[i][j] == '#' and not ship[i][j]:
            cnt = 1
            for k in range(j + 1, j + 3):
                if 0 <= k < 10 and s[i][k] == '#' and not ship[i][k]:
                    cnt += 1
            if cnt == 3:
                ship3 += 1
                for k in range(j, j + 3):
                    ship[i][k] = ship3 + 1
                    mp[ship3 + 1] = 3
if ship3 < 2:
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#' and not ship[i][j]:
                cnt = 1
                for k in range(i + 1, i + 3):
                    if 0 <= k < 10 and s[k][j] == '#' and not ship[k][j]:
                        cnt += 1
                if cnt == 3:
                    ship3 += 1
                    for k in range(i, i + 3):
                        ship[k][j] = ship3 + 1
                        mp[ship3 + 1] = 3

# Check for three ships of size 2
ship2 = 0
for i in range(10):
    for j in range(10):
        if j < 9 and s[i][j] == '#' and s[i][j + 1] == '#' and not ship[i][j] and not ship[i][j + 1]:
            ship2 += 1
            ship[i][j] = ship2 + 3
            ship[i][j + 1] = ship2 + 3
            mp[ship2 + 3] = 2
if ship2 < 3:
    for i in range(10):
        for j in range(10):
            if i < 9 and s[i][j] == '#' and s[i + 1][j] == '#' and not ship[i][j] and not ship[i + 1][j]:
                ship2 += 1
                ship[i][j] = ship2 + 3
                ship[i + 1][j] = ship2 + 3
                mp[ship2 + 3] = 2

# Check for single ships of size 1
ship1 = 0
for i in range(10):
    for j in range(10):
        if s[i][j] == '#' and not ship[i][j]:
            ship1 += 1
            ship[i][j] = ship1 + 6
            mp[ship1 + 6] = 1

# Process queries
q = int(input())
un = 10
hit = 0
sunk = 0

for _ in range(q):
    query = input().split()
    cmd = query[0]

    if cmd == "SHOW":
        print(un, hit, sunk)
    else:
        x, y = map(int, query[1:])
        if s[x][y] == '#':
            tau = ship[x][y]
            mp[tau] -= 1
            if mp[tau] <= 0:
                sunk += 1
            else:
                hit += 1
