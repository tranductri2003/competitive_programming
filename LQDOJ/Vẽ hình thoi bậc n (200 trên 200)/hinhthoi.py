n=int(input())

for i in range(1,2*n):
    if i<=n:
        for solanindaucach in range(1,n-i+1):
            print(" ",end="")
        for solanindausao in range(1,2*i):
            print("*",end="")
    else:
        for solanindaucach in range(1,i-n+1):
            print(" ",end="")
        for solanindausao in range(1,4*n-2*i):
            print("*",end="")
    print("\n")