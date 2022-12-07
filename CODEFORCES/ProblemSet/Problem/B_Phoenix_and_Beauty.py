import math
"""
For an array to be beautiful for some k, the array must be periodic with period k. If there exists more than k distinct numbers in the array a, there is no answer and we print -1 (because the array cannot be periodic with period k). Otherwise, we propose the following construction.

Consider a list of all the distinct numbers in array a. If there are less than k of them, we will append some 1s (or any other number) until the list has size k. We can just print this list n times. The length of our array b is nk, which never exceeds 104. Array b can always be constructed by inserting some numbers into array a because every number in a corresponds to one list.

Time complexity for each test case: O(nlogn+nk)
"""
t=int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))

    temp=list(set(a))
    if len(temp)>k:
        print(-1)
    else:
        for i in range(k-len(temp)):
            temp.append(1)
        res=temp*n
        print(len(res))
        print(*res)
        
        