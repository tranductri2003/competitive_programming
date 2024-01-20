N = int(input())
t = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

able = [0]*N
able[0] = a[0]

for i in range(1,N):
    able[i] = able[i-1]+a[i]


res =0
lose = False

if a[0]<b[0]:
    lose = True
else:
    for i in range(N-1,-1,-1):
        if able[i]>=b[i]:
            need = max(0, b[i]-a[i])
            res+=need*t[i-1]
            able[i-1]-=need
            a[i-1]-=need
        else:
            lose = True
            break
    
if lose:
    print(-1)
else:
    print(res)
