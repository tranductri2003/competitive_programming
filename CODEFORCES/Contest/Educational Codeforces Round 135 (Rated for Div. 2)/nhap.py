import sys
from math import sqrt, gcd, factorial, ceil, floor, pi, inf
from collections import deque, Counter, OrderedDict
from heapq import heapify, heappush, heappop
#sys.setrecursionlimit(10**6)

#======================================================#
input = lambda: sys.stdin.readline()
I = lambda: int(input().strip())
S = lambda: input().strip()
M = lambda: map(int,input().strip().split())
L = lambda: list(map(int,input().strip().split()))
#======================================================#

#======================================================#
def primelist():
    L = [False for i in range(10**9)]
    primes = [False for i in range(10**9)]
    for i in range(2,10**9):
        if not L[i]:
            primes[i]=True
            for j in range(i,10**9,i):
                L[j]=True
    return primes
def isPrime(n):
    p = primelist()
    return p[n]
#======================================================#
def bst(arr,x):
    low,high = 0,len(arr)-1
    ans = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            ans = mid
            low = mid+1
        else:
            high = mid-1
    return ans

#======================================================#

def fx(x):
    ans = 0
    while x>0:
        ans+=1
        x//=10
    return ans

for _ in range(I()):
    n = I()
    a = L()
    b = L()
    d = {}
    for i in range(n):
        if a[i] in d.keys():
            d[a[i]].append(i)
        else:
            d[a[i]]=[i]
    p,q = [True for i in range(n)],[True for i in range(n)]
    for i in range(n):
        if b[i] in d.keys():
            if len(d[b[i]]):
                q[i]=False
                p[d[b[i]].pop()]=False
    g,h=[0 for i in range(10)],[0 for i in range(10)]
    ans=0
    for i in range(n):
        if p[i]:
            if a[i]<10:
                g[a[i]]+=1
            else:
                g[fx(a[i])]+=1
                ans+=1
        if q[i]:
            if b[i]<10:
                h[b[i]]+=1
            else:
                h[fx(b[i])]+=1
                ans+=1
    for i in range(9,1,-1):
        if g[i]==h[i]:
            continue
        elif g[i]<h[i]:
            h[1]+=h[i]-g[i]
            ans+=h[i]-g[i]
        else:
            g[1]+=g[i]-h[i]
            ans+=g[i]-h[i]
    print(ans)
    
    
    
    
    
    
    
