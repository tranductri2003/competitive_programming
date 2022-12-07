n=int(input())

if n%2==0:
    print(round(-(n/2)))
else:
    print(round(-(n//2)+n))