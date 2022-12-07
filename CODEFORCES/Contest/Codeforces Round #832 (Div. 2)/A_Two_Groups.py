# A Python code.

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    am = []
    duong = []
    for num in a:
        if num < 0:
            am.append(num)
        else:
            duong.append(num)
    print(max(abs(sum(am))-abs(sum(duong)), abs(sum(duong))-abs(sum(am))))
