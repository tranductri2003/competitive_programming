from random import randint


def solve2(n,k,a):
    res=0
    for i in range(k):
        if a[i]>k:
            res+=1
    return res
def solve1(n,k,a):
    b=a.copy()
    res=0
    b.sort()
    b=b[:k]
    res=0
    for i in range(k):
        if a[i] not in b:
            res+=1
    return res
t=int(input())
for _ in range(t):
    # n=randint(1,100)
    # k=randint(1,n)
    # a=[randint(1,n) for _ in range(n)]
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    print(solve1(n,k,a),solve2(n,k,a))
    if solve1(n,k,a)!=solve2(n,k,a):
        print(n,k)
        for num in a:
            print(num,end=" ")
        break

