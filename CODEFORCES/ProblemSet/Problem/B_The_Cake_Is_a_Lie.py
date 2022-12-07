testcase=int(input())
"""
Note that whichever path you choose, the total cost will be the same. If you know that the cost is the same, then it's not hard to calculate it. It's equal to n⋅m−1. So the task is to check: is k equal to n⋅m−1 or not.

The constant cost may be proved by induction on n+m: for n=m=1 cost is 1⋅1−1=0. For a fixed (n,m), there are only two last steps you can make:

either from (n,m−1) with cost n: the total cost is n⋅(m−1)−1+n = n⋅m−1
or from (n−1,m) with cost m: the total cost is (n−1)⋅m−1+m = n⋅m−1.
So, whichever path you choose, the total cost is the same."""
for test in range(testcase):
    n,m,k=list(map(int,input().split()))
    res=0
    res=n*m-1
    if res==k:
        print("YES")
    else:
        print("NO")
    """
    move right to the cell (x,y+1) — it costs x burles;
    move down to the cell (x+1,y) — it costs y burles.
    """
    
    """In the second, third and fourth test cases, 
    there are two paths from (1,1) to (2,2): (1,1) → (1,2) → (2,2) or (1,1) → (2,1) → (2,2).
    Both costs 1+2=3 burles, so it's the only amount of money you can spend.
    """

        
        