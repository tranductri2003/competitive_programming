"""Nastia has 2 positive integers A and B. She defines that:

The integer is good if it is divisible by A⋅B;
Otherwise, the integer is nearly good, if it is divisible by A.
For example, if A=6 and B=4, the integers 24 and 72 are good, the integers 6, 660 and 12 are nearly good, the integers 16, 7 are neither good nor nearly good.

Find 3 different positive integers x, y, and z such that exactly one of them is good and the other 2 are nearly good, and x+y=z.
"""
t=int(input())
for _ in range(t):
    a,b=list(map(int,input().split()))

    #Số tốt là bội của a.b
    #Hai số gần tốt là bội của a mà khác bội của a.b
    if b==1: 
        print("NO")
    else:
        print("YES")
        # if b==2: 
        #     # 7 2 => 7 21 28
        #     print(a,3*a,4*a)
        # else:
        #     print(a,(b-1)*a,a*b)
        print(a,a*b,a*(b+1))
        
        
        