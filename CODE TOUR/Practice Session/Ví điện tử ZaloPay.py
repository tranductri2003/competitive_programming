n = int(input())
res = (n+n**2)*n/2-n*(n-1)/2
res = res % 2027


if "." not in str(res):
    print(res)
else:
    print(str(res)[:-2])
