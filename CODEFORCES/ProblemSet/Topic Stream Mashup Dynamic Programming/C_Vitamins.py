from collections import defaultdict

check=defaultdict(lambda:10**9)
n=int(input())
for i in range(n):
    s,c=input().split()
    c=list(c)
    c.sort()
    c="".join(c)
    s=int(s)
    check[c]=min(check[c],s)
res=min(check['A']+check['B']+check['C'],
        check['AB']+check['C'],check['AB']+check['BC'],check['AB']+check['AC'],
        check['AC']+check['B'],check['AC']+check['BC'],check['AC']+check['AB'],
        check['BC']+check['A'],check['BC']+check['AB'],check['BC']+check['AC'],
        check['ABC']
        )
if res>=10**9:
    print(-1)
else:
    print(res)

