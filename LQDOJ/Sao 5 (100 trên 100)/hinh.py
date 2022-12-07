n=int(input())

for num in range(n,0,-1):
    print(str(" ")*(n-num)                    +str("*")*(2*num-1))