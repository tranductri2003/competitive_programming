n=8
def numToCoordinate(N):
    x=(N-1)%n
    y=(N-1)//n
    return x,y


position=[]
def possiblePosition(N):
    a=[]
    x,y=numToCoordinate(N)
    if x>=1 and y>=2:
        a.append(N-2*n-1)
    if x<=n-2 and y>=2:
        a.append(N-2*n+1)
    if x>=2 and y>=1:
        a.append(N-n-2)
    if x<=n-3 and y>=1:
        a.append(N-n+2)
    if x>=2 and y<=n-2:
        a.append(N+n-2)
    if x>=1 and y<=n-3:
        a.append(N+2*n-1)
    if x<=n-2 and y<=n-3:
        a.append(N+2*n+1)
    if x<=n-3 and y<=n-2:
        a.append((N+n+2))
    return a
N=int(input())
position=possiblePosition(N)
print(position)