
# Python program to print all
# primes smaller than or equal to
# n using Sieve of Eratosthenes



a=[]
dp=[0]*(10**6+1)
check=[0]*(10**6+1)
def SieveOfEratosthenes(n):
 
    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
 
    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            a.append(p)
 
 
# Driver code

n = 10**6
SieveOfEratosthenes(n)


stack=0
for num in a:
    stack+=1
    dp[num]=stack
    check[num]=1

for i in range(1,10**6+1):
    if dp[i]<dp[i-1]:
        dp[i]=dp[i-1]

testcase=int(input())

for test in range(testcase):
    L,R=list(map(int,input().split()))
    L=min(L,R)
    R=max(L,R)
    res=dp[R]-dp[L]
    if check[L]==1 or check[R]==1:
        res+=1
    print(res)
    
