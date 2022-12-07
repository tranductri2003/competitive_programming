
# Python program to print all
# primes smaller than or equal to
# n using Sieve of Eratosthenes




check=[0]*(10**6+1)
check[2]=1
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
            check[p]=1
 
 
# Driver code

n = 10**6
SieveOfEratosthenes(n)


testcase=int(input())

for test in range(testcase):
    L,R=list(map(int,input().split()))
    if L>R:
        L,R=R,L
    print(sum(check[L:R+1]))