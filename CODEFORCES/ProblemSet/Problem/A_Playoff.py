# if x+y is odd, the athlete with the lower index wins (i. e. if x<y, then x wins, otherwise y wins);
# if x+y is even, the athlete with the higher index wins.

t=int(input())

for _ in range(t):
    n=int(input())
    print(2**n-1) 