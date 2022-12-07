# The answer is a1|a2|⋯|an. Here is the proof:

# Let m=a1|a2|⋯|an. After an operation, the value m won't change.

# Since, a1|a2|⋯|an≤a1+a2+⋯+an, the sum of the array has a lower bound of m. And this sum can be constructed easily: for all i∈[1,n−1], set ai+1 to ai|ai+1 and ai to 0.
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(n):
        res = res | a[i]
    print(res)
