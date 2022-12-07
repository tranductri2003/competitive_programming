
t = int(input())
for _ in range(t):
    s = input()
# In the first line print two integers cost, m,
# where cost is the minimum total cost of the path,
# and m is the maximum number of jumps Polycarp must make to get to n-th tiles for the minimum total cost.
    num = []
    for i in range(len(s)):
        num.append(ord(s[i])-96)
    # print(num)

    if num[0] == num[-1]:
        res = [1]
        for i in range(1, len(num)-1):
            if num[i] == num[0]:
                res.append(i+1)
        res.append(len(s))

        cost = 0
        for i in range(len(res)-1):
            cost += abs(ord(s[res[i]-1])-ord(s[res[i+1]-1]))

        print(cost, len(res))
        print(*res)
    elif num[0] > num[-1]:
        data = []
        for i in range(1, len(num)-1):
            if num[-1] <= num[i] <= num[0]:
                data.append((num[i], i+1))
        data.sort(reverse=True)
        res = [1]
        for num in data:
            res.append(num[1])
        res.append(len(s))

        cost = 0
        for i in range(len(res)-1):
            cost += abs(ord(s[res[i]-1])-ord(s[res[i+1]-1]))

        print(cost, len(res))
        print(*res)
    else:
        data = []
        for i in range(1, len(num)-1):
            if num[0] <= num[i] <= num[-1]:
                data.append((num[i], i+1))
        data.sort()
        res = [1]
        for num in data:
            res.append(num[1])
        res.append(len(s))

        cost = 0
        for i in range(len(res)-1):
            cost += abs(ord(s[res[i]-1])-ord(s[res[i+1]-1]))

        print(cost, len(res))
        print(*res)
