
t=int(input())

for _ in range(t):
    m,k,a1,a2 = list(map(int,input().split()))
    if a1 >= m or (m % k <= a1 and m // k <= a2):
        print(0)
    else:
        temp2 = min(m // k, a2)
        temp1 = min(m - k * temp2, a1)
        res = m - temp1 - k * temp2
        if res % k == 0:
            print(res // k)
        elif (k - res % k) <= temp1:
            print((res // k) + 1)
        else:
            print((res // k) + (res % k))