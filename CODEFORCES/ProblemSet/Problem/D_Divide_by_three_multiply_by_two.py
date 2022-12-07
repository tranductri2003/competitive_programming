n=int(input())
a=list(map(int,input().split()))
current=[]
current.append(min(a))
a.pop(a.index(min(a)))

while True:
    if (current[-1]/3) in a or (current[-1]*2) in a:
        if (current[-1]*2) in a:
            pos=a.index(current[-1]*2)
            current.append(a[pos])
            a.pop(pos)
        else:
            pos=a.index(current[-1]/3)
            current.append(a[pos])
            a.pop(pos)
    else:
        break
while True:
    if (current[0]*3) in a or (current[0]/2) in a:
        if (current[0]*3) in a:
            pos=a.index(current[0]*3)
            current.insert(0,a[pos])
            a.pop(pos)
        else:
            pos=a.index(current[0]/2)
            current.insert(0,a[pos])
            a.pop(pos)
    else:
        break
print(*current)