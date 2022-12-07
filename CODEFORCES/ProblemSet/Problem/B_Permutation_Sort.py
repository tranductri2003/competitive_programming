"""To solve the problem, it is enough to consider several cases:

if the array is already sorted, the answer is 0;
if a[1]=1 (or a[n]=n), then you can sort the array in one operation by selecting the subarray [1,n−1] (or [2,n]);
if a[1]=n and a[n]=1, you can perform the sequence of operations [1,n−1], [2,n] and [1,n−1] and sort the array on each of them (you can't do it faster since you can't move both n to position n and 1 to position 1 in only 2 operations);
otherwise, the array can be sorted in 2 operations.
"""

testcase=int(input())
for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))
    if a==sorted(a):
        print(0)
    else:
        # 4 2 3 1
        # 4 1 2 3
        # 1 2 4 3
        # 1 2 3 4

        # 4 5 2 1 3
        # 1 2 4 5 3
        # 1 2 3 4 5
        
        # 1 3 4 2 5
        # 1 2 3 4 5

        # 2 3 1
        # 2 1 3
        # 1 2 3
        
        if a.index(1) == 0 or a.index(n)== n-1:
            print(1)
        else:
            if a.index(1) == n-1 and a.index(n)==0:
                print(3)
            else:
                print(2)

