import math
from collections import defaultdict

t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    student = list(map(int, input().split()))
    student.sort()

    temp = 1
    for i in range(1, m+1):
        temp = math.lcm(temp, i)
    if temp in student:
        print(0)
    else:
        if m % 2 == 0:
            rest = m//2
        else:
            rest = m//2+1
        check = defaultdict(lambda: False)
        data = []
        i = 0
        while rest != 0 and i < n:
            if student[i] < (m//2+1):
                i += 1
            else:
                if student[i] <= m:
                    if check[student[i]] == False:
                        check[student[i]] = True
                        rest -= 1
                        data.append(student[i])
                    else:
                        pass
                    i += 1
                else:
                    temp = []
                    j = 1
                    while j**2 <= student[i]:
                        if j**2 == student[i]:
                            temp.append(student[i])
                            break
                        else:
                            if student[i] % j == 0:
                                temp.append(j)
                                temp.append(student[i]//j)
                            j += 1
                    for num in temp:
                        if n//2+1 <= num <= n and check[num] == False:
                            check[num] = True
                            rest -= 1
                            data.append(student[num])
                    i += 1
        if rest != 0:
            print(-1)
        else:
            print(max(data)-min(data))
