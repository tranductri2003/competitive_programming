

def solve(n):
    if n==1:
        return "2"
    else:
        if n%2==0:
            return "("+solve(n//2)+")^2"
        else:
            return "(2*"+solve(n-1)+")"
    
t=int(input())
for _ in range(t):
    n=int(input())
    print(solve(n))