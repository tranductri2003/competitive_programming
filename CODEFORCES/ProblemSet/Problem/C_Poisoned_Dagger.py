"""k+∑i=1  n−1min(k,ai+1−ai)
"""
"""
Let's find out the total damage for a fixed value of k. Since the effect
of the poison from the
i-th attack deals damage min(k,ai+1−ai) seconds for i<n and k seconds for i=n,
then the total damage is k+∑i=1n−1min(k,ai+1−ai). 
We can see that the higher the value of k, the greater the total sum.
So we can do a binary search on k and find the minimum value 
when the sum is greater than or equal to h.

"""
testcase=int(input())
for test in range(testcase):
    n,h=list(map(int,input().split()))
    a=list(map(int,input().split()))
    left=1
    right=2*h+1
    while left<=right:
        k=(left+right)//2
        sum=k
        for i in range(0,n-1):
            sum+=min(k,a[i+1]-a[i])
        if sum<h:
            left=k+1
        else:
            right=k-1

    print(right+1)
        
        