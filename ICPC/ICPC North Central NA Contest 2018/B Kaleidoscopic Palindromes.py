"""
Input
Input consists of three space-separated integers: a, b, and k. The input satisfies the following constraints:

0≤a≤b≤2000000,2≤k≤100000.
Output
Output the quantity of numbers between a and b inclusive which are palindromes in every base j, for 2≤j≤k.
"""


def check(i,j):
    a=list()
    while i !=0:
        a.append(i%j)
        i=i//j
    if a==a[::-1]:
        return True
    else:
        return False

    


a,b,k=list(map(int,input().split()))  

res=0
for i in range(a,b+1):
    for j in range(2,k+1):
        if check(i,j)==False:
            break
    else:
        res+=1
    


print(res)


n=int(input())
for i in range(0,n):
    x,fx=list(map(int(input()).split()))