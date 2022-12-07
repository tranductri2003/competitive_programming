def gcd(a,b):
    if a==0:
        print (b)
    else:
        gcd(b%a,a)
        
        
a=int(input())
b=int(input())
gcd(a,b)