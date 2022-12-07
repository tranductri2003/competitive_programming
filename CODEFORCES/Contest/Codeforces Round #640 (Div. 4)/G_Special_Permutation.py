# For a given number n (n≥2), 
# find a permutation p in which absolute difference (that is, the absolute value of difference) of any two neighboring (adjacent) elements is between 2 and 4, inclusive. Formally, find such permutation p that 2≤|pi−pi+1|≤4 for each i (1≤i<n).





t=int(input())

for _ in range(t):
    n=int(input())
# If n<4 then there is no answer. You can do some handwork to be sure. Otherwise, the answer exists and there is one simple way to construct it: firstly, let's put all odd integers into the answer in decreasing order, then put 4, 2, and all other even numbers in increasing order.
    if n<4:
        print(-1)
    else:    
        res=[]
        if n%2==0:
            for i in range(n-1,0,-2):
                res.append(i)
            res+=[4,2]
            for i in range(6,n+1,2):
                res.append(i)
        else:
            for i in range(n,0,-2):
                res.append(i)
            res+=[4,2]
            for i in range(6,n,2):
                res.append(i)
        print(*res)