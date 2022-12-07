testcase=int(input())
for i in range(0, testcase):
    n=int(input())
    if n%2==1:
        print(n//2, end=" ")
        print(n//2+1)
    else:
        k=n//2
        if k%2==1:
            print(k//2-1,end=" ")
            print(k//2+2)
        else:
            k=3
            while k<n:
                if n%k==0:
                    print(n//k-k//2,end=" ")
                    print(n//k+k//2)
                    break
                k+=2

