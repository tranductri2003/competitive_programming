import random

def is_Prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n!=int(n):
        return False
    n=int(n)
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  

import math



t=int(input())
for _ in range(t):
    l,r = list(map(int,input().split()))
    
    exist = -1
    for i in range(l,r+1):
        if i %2==0 and i!=2:
            exist = i
            break
            
    if exist!=-1:
        print(2, i-2)
    else:
        for i in range(l,r+1):
            if is_Prime(i)==True or i==1:
                pass
            else:
                for j in range(2,int(math.sqrt(i))+1):
                    if i%j==0:
                        print(j,i-j)
                        break
                break
        else:
            print(-1)
