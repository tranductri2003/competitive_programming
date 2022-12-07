# Suppose you have an integer v. In one operation, you can:

# either set v=(v+1)mod32768
# or set v=(2⋅v)mod32768.


n=int(input())
a=list(map(int,input().split()))

for num in a:
    res=15
    for add in range(0,16):
        for mul in range(0,16):
            if (num+add)*(2**mul)%32768==0:
                res=min(res,add+mul)
    print(res,end=" ")