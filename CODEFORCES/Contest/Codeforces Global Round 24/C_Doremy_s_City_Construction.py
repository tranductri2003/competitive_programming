
from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # print(sorted(a))
    # if len(set(a)) == 1:
    #     print(n//2)
    # else:
    #     maxx = max(a)
    #     soluongmax = 0
    #     soluongnhohon = 0
    #     for num in a:
    #         if num == maxx:
    #             soluongmax += 1
    #         else:
    #             soluongnhohon += 1
    #     print(soluongnhohon*soluongmax+(soluongmax-1))
    a.sort()
    # print(a)
    data = []
    count = Counter(a)
    for num in count:
        data.append(count[num])
    # print(data)
    if len(data) == 1:
        print(n//2)
    else:
        res = 0
        tong = sum(data)
        temp = 0
        for i in range(0, len(data)):
            temp += data[i]
            res = max(res, temp*(tong-temp))
        print(res)
