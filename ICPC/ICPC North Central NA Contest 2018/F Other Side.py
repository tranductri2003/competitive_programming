w,s,c,k=list(map(int,input().split()))  


if w+c>k and s>k:
    print("NO")
    quit()
if s<k:
    print("YES")
    quit()
if w+c<k:
    print("YES")
    quit()
if w+c==k and s<=2*k:
    print("YES")
    quit()
if s==k and (w+c)<=2*k:
    print("YES")
    quit()
else:
    print("NO")