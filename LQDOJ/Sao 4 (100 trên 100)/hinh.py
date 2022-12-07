n=int(input())

for num in range(1,n+1):
    print(str(" ")*(n-num)+str("*")*(num*2-1))