# Python3 program to print
# primes smaller than n using
# Sieve of Sundaram.

# Prints all prime numbers smaller
def SieveOfSundaram(n,listsnt):
	# In general Sieve of Sundaram,
	# produces primes smaller
	# than (2*x + 2) for a number
	# given number x. Since we want
	# primes smaller than n, we
	# reduce n to half
	nNew = int((n - 1) / 2);

	# This array is used to separate
	# numbers of the form i+j+2ij
	# from others where 1 <= i <= j
	# Initialize all elements as not marked
	marked = [0] * (nNew + 1);

	# Main logic of Sundaram. Mark all
	# numbers of the form i + j + 2ij
	# as true where 1 <= i <= j
	for i in range(1, nNew + 1):
		j = i;
		while((i + j + 2 * i * j) <= nNew):
			marked[i + j + 2 * i * j] = 1;
			j += 1;

	# Since 2 is a prime number
	if (n > 2):
		listsnt.append(2)

	# Print other primes. Remaining
	# primes are of the form 2*i + 1
	# such that marked[i] is false.
	for i in range(1, nNew + 1):
		if (marked[i] == 0):
			listsnt.append(2 * i + 1)


# Driver Code


list=list();


n=int(input())




SieveOfSundaram(n,list);
for num in list:
    print(num, end=" ")