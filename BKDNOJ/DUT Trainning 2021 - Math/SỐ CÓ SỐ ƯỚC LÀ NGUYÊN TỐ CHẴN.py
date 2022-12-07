
# Python program to print all
# primes smaller than or equal to
# n using Sieve of Eratosthenes
from os import replace


a=[0]
 
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
if __name__ == '__main__':
    n = 10**6
    SieveOfEratosthenes(n)
             
# Driver code
n = 10**6

SieveOfEratosthenes(n)

def upper_bound(my_list, key):
    large = len(my_list) -1
    small = 0

    while (small <= large):
        mid = (small + large) // 2
        if my_list[mid] < key:
            small = mid + 1
        elif my_list[mid] > key:
            large = mid - 1
        else:
            return mid
    if my_list[mid]>key:
        return mid
    else:
        return mid+1

def lower_bound(my_list, key):
    large = len(my_list) -1
    small = 0

    while (small <= large):
        mid = (small + large) // 2
        if my_list[mid] < key:
            small = mid + 1
        elif my_list[mid] > key:
            large = mid - 1
        else:
            return mid
    if my_list[mid]<key:
        return mid
    else:
        return mid-1

testcase=int(input())

for test in range(testcase):
    L,R=list(map(int,input().split()))
    L=min(L,R)
    R=max(L,R)
    
    l=upper_bound(a,L)
    r=lower_bound(a,R)

    print(r-l+1)
    
