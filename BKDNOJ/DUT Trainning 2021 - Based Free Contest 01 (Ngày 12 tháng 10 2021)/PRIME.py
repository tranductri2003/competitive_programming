 
def SieveOfEratosthenes(n):
    mangsnt=list()
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
            mangsnt.append(p)
    return mangsnt
 
a=SieveOfEratosthenes(10**7)

testcase=int(input())

for test in range(0,testcase):
    l,r=list(map(int,input().split()))
    sum=0
    quan=0
    for num in a:
        if l<=num<=r:
            sum+=num
            quan+=1
    print(sum/quan)


    