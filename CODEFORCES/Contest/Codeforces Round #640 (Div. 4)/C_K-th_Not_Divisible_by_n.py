# You are given two positive integers n and k. Print the k-th positive integer that is not divisible by n.


#In số thứ k mà không chia hết cho n

t=int(input())

for _ in range(t):
    n,k=list(map(int,input().split()))
    #Số n thì sau mỗi n số thì sẽ có n-1 số không chia hết cho n
    
    if n==k:
        res=n+1
    elif n>k:
        res=k
    else:
        if k%(n-1)==0: #Ngay cạnh
            res=k//(n-1)*n-1
        else:
            res=k//(n-1)*n  
            res+=k-res//n*(n-1)
    print(res)
    