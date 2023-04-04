t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    prefixSum = [0]
    temp = 0
    for num in a:
        temp += num
        prefixSum.append(temp)
    stop = False
    while stop == False:
        l = 1
        r = n
        while r-l >= 1:
            m = (l+r)//2
            data = [i for i in range(l, m+1)]
            data.insert(0, m-l+1)
            print("?", *data)
            temp = int(input())
            if temp != prefixSum[m]-prefixSum[l-1]:
                r = m
            else:
                l = m+1
        print("!", l)
        stop = True
