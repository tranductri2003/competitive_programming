def dequy(m,v):
    if m==0:
        if v==0:
            return 1
        else:
            return 0
    
    else:
        if m>v:
            return dequy(m-1,v)
        else:
            return dequy(m-1,v)+dequy(m,v-m)

n=int(input())
print(dequy(n,n))