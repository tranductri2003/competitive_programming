
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

prefixSum=[0]
sum=0
for num in check:
    sum=sum+num
    prefixSum.append(sum)

testcase=int(input())

for test in range(testcase):
    L,R=list(map(int,input().split()))
    if L>R:
        L,R=R,L
    print(prefixSum[R+1]-prefixSum[L])


"""
#include<bits/stdc++.h>

using namespace std;

bool nguyento[1000007];

void solve(){
    int  l, r;
    cin>>l>>r;
    if (l>r) swap(l,r);
    int result=0;
    for (int i=l ; i<=r; i++){
        if (!nguyento[i]){
            result++;
        }
    }
    cout<<result<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    nguyento[1]=1;
    for (int i=1; i<1000007; i++){
        if (nguyento[i]==0){
            for (int count=2*i; count<1000007; count+=i){
                nguyento[count]=1;
            }
        }
    }
    int t;
    cin>>t;

    for (int i =0 ;i<t ; i++){
        solve();
    }
    return 0; 
}
"""