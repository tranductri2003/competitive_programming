n=int(input())
A=0
B=0

for i in range(n):
    x,y=list(map(int,input().split()))
    if x>y:
        A+=x+y
    if x<y:
        B+=x+y
    if x==y:
        A+=x
        B+=y
print(A,B)