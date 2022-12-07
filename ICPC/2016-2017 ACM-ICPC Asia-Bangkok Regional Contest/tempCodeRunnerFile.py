
from collections import defaultdict


# Create an array for memoization
f = defaultdict(lambda:0)
 
# Returns n'th fibonacci number using table f[]
def fib(n) :
    # Base cases
    if (n == 0) :
        return 0
    if (n == 1 or n == 2) :
        f[n] = 1
        return (f[n])
 
    # If fib(n) is already computed
    if (f[n]) :
        return f[n]
 
    if( n & 1) :
        k = (n + 1) // 2
    else :
        k = n // 2
 
    # Applying above formula [Note value n&1 is 1
    # if n is odd, else 0.
    if((n & 1) ) :
        f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1))
    else :
        f[n] = (2*fib(k-1) + fib(k))*fib(k)
 
    return f[n]
 
 






def multiply(a, b):

	mul = [[0 for x in range(3)]
			for y in range(3)];
	for i in range(3):
		for j in range(3):
			mul[i][j] = 0;
			for k in range(3):
				mul[i][j] += a[i][k] * b[k][j];


	for i in range(3):
		for j in range(3):
			a[i][j] = mul[i][j]; 
	return a



def power(F, n):
	M = [[1,2,1],[2,3,2],[0,0,1]]

	# Multiply it with initial values i.e
	# with F(0) = 0, F(1) = 1, F(2) = 1
	if (n == 1 or n==0):
		return 

	power(F, int(n / 2));

	F = multiply(F, F);

	if (n % 2 != 0):
		F = multiply(F, M);

	return


    

    
t=int(input())
for _ in range(t):

    L,R,K=list(map(int,input().split()))
    t3=fib(K-3+2)
    t2=fib(K-2+2)
    t1=fib(K-1+2)

    matran1=[[t3,t2,t3],[t2,t1,t2],[0,0,1]]
    matran2=[[t3,t2,t3],[t2,t1,t2],[0,0,1]]
    matranketqua1=[[1,2,1]],[0,0,0],[0,0,0]
    matranketqua2=[[1,2,1]],[0,0,0],[0,0,0]
    

    power(matran1,R//K)
    power(matran2,(L-1)//K)
    
    multiply(matranketqua1,matran1)
    multiply(matranketqua2,matran2)
    for i in range(3):
        print(matranketqua1[i])
    
    for i in range(3):
        print(matranketqua2[i])
