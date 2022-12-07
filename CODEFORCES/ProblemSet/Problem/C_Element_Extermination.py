t=int(input())
# Tới max tăng đều hoặc tới min giảm đều thì in ra NO
# Còn lại là YES
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    # if n==1:
    #     print("YES")
    # else:
    #     check1=False
    #     check2=False
        
    #     indexMax=a.index(n)
    #     indexMin=a.index(1)
        
    #     for i in range(0,indexMax):
    #         if a[i+1]==a[i]+1:
    #             pass
    #         else:
    #             check1=True  
    #             break
        
    #     for i in range(n-1,indexMin,-1):
    #         if a[i-1]==a[i]-1:
    #             pass
    #         else:
    #             check2=True
    #             break
    #     if (check1==False or check2==False) and indexMin>indexMax:
    #         print("NO")
    #     else:
    #         print("YES")
    if a[0]<a[-1]:
        print("YES")
    else:
        print("NO")