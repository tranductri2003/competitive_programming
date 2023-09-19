
def totalPrimeFactors(n):
	
	count = 0;

	if ((n % 2) == 0):
		count += 1;
		while ((n % 2) == 0):
			n //= 2;

	i = 3;
	while (i * i <= n):
		
		if ((n % i) == 0):
			count += 1;
			while ((n % i) == 0):
				n //= i;
		i += 2;

	if (n > 2):
		count += 1;

	return count;

def countPairs(G, L):

	if (L % G != 0):
		return 0;

	div = int(L / G);

	return (1 << totalPrimeFactors(div));

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

M = int(input())
C = list(map(int,input().split()))
D = list(map(int,input().split()))

L=1
G=1
for i in range(N):
    L*=A[i]**B[i]

for i in range(M):
    G*=C[i]**D[i]
    
print(countPairs(G, L)%998244353)

