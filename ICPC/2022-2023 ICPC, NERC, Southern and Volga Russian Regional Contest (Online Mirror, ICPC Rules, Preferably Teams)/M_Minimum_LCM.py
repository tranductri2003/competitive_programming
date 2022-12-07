
import math
t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print(n//2, n//2)
    else:
        data = []
        for i in range(1, int(math.sqrt(n))+1):
            if i**2 == n:
                data.append(i)
                break
            else:
                if n % i == 0:
                    data.append(i)
                    data.append(n//i)
        data.sort()
        current = 1
        temp = 10**9
        for num in data:
            if num != n:
                if math.lcm(num, n-num) < temp:
                    current = num
                    temp = math.lcm(num, n-num)
        print(current, n-current)
