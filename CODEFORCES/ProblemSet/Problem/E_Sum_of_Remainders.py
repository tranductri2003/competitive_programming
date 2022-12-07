#n,m=list(map(int,input().split()))
#Calculate the value of the sum: n mod 1 + n mod 2 + n mod 3 + ... + n mod m. 
# As the result can be very large, 
# you should print the value modulo 109 + 7 (the remainder when divided by 109 + 7).

# for i in range(1,151):
#     print(f"100 %{i}={100%i}")

# import sys, math
# input=sys.stdin.readline
# INF=int(1e9)+7
 
# def solve(): 
#     n,m=map(int,input().split()) 
#     result=n*m
#     result%=INF 
#     cur=min(n,m)
#     while cur:
#         now=n//cur
#         next_cur=n//(now+1) 
#         result-=((cur-next_cur)*(cur+next_cur+1)//2)*now
#         result%=INF
#         print(now,cur,next_cur,result,((cur-next_cur)*(cur+next_cur+1)//2)*now)
#         cur=next_cur
        
n,m=list(map(int,input().split()))
res=n*m
cur=min(n,m)
while cur:
    now=n//cur
    next_cur=n//(now+1)
    res-=((cur-next_cur)*(cur+next_cur+1)//2)*now
    cur=next_cur
print(res%(10**9+7))
    