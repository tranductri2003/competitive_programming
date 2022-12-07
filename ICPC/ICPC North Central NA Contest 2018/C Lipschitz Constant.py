"""
Today you are doing your calculus homework, and you are tasked with finding a Lipschitz constant for a function f(x), which is defined for N integer numbers x and produces real values. Formally, the Lipschitz constant for a function f is the smallest real number L such that for any x and y with f(x) and f(y) defined we have:

|f(x)−f(y)|≤L⋅|x−y|.
Input
The first line contains N – the number of points for which f is defined. The next N lines each contain an integer x and a real number z, which mean that f(x)=z. Input satisfies the following constraints:

2≤N≤200000.

All x and z are in the range −109≤x,z≤109.

All x in the input are distinct.

Output
Print one number – the Lipschitz constant. The result will be considered correct if it is within an absolute error of 10−4 from the jury’s answer.
"""

import math 

a=dict()
n=int(input())
for i in range(0,n):
    x,fx=list(map(float,(input()).split()))
    a[x]=fx

a=sorted(a.items())  #Sort theo cả values và keys


L=-999999
for i in range(0,n-1):
    L=max(L,abs((a[i+1][1]-a[i][1])/(a[i+1][0]-a[i][0])))

print(L)
