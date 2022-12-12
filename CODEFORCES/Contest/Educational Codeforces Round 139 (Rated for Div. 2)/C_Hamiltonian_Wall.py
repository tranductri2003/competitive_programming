

t = int(input())
for _ in range(t):
    n = int(input())
    soLan = 0
    s1 = input()
    soLan += s1.count("B")
    s2 = input()
    soLan += s2.count("B")
    s = []
    for i in range(2):
        s.append([])
        for j in range(n):
            if i == 0:
                s[i].append(s1[j])
            else:
                s[i].append(s2[j])
    if n == 1:
        print("YES")
    else:
        attemp1 = False
        attemp2 = False

        # Thu lan 1
        i = 0
        j = 0
        if s[i][j] == "B":
            count1 = 1
            while True:
                if s[1-i][j] == "B":
                    count1 += 1
                    i = 1-i
                    if j+1 == n:
                        break
                    if s[i][j+1] == "B":
                        j += 1
                        count1 += 1
                    else:
                        break
                else:
                    if j+1 == n:
                        break
                    if s[i][j+1] == "B":
                        j += 1
                        count1 += 1
                    else:
                        break
            if count1 == soLan:
                attemp1 = True

        # Thu lan 2
        i = 1
        j = 0
        if s[i][j] == "B":
            count1 = 1
            while True:
                if s[1-i][j] == "B":
                    count1 += 1
                    i = 1-i
                    if j+1 == n:
                        break
                    if s[i][j+1] == "B":
                        j += 1
                        count1 += 1
                    else:
                        break
                else:
                    if j+1 == n:
                        break
                    if s[i][j+1] == "B":
                        j += 1
                        count1 += 1
                    else:
                        break
            if count1 == soLan:
                attemp2 = True

        if attemp1 == True or attemp2 == True:
            print("YES")
        else:
            print("NO")
