# Given an array a of length n and an integer k, find the number of indices 1≤i≤n−k such that the subarray [ai,…,ai+k] with length k+1 (not with length k) has the following property:

# If you multiply the first element by 20, the second element by 21, ..., and the (k+1)-st element by 2k, then this subarray is sorted in strictly increasing order.
# More formally, count the number of indices 1≤i≤n−k such that
# 20⋅ai<21⋅ai+1<22⋅ai+2<⋯<2k⋅ai+k.


t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    check = []
    stack = 1
    for i in range(1, n):
        if a[i-1] < 2*a[i]:
            stack += 1
            if i == n-1:
                check.append(stack)
        else:
            check.append(stack)
            stack = 1

    res = 0
    for num in check:
        res += max(0, num-k)
    print(res)
