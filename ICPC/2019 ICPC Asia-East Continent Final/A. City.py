n, m = list(map(int, input().split()))
kVer = 0
tempVer = n-1
while tempVer > 0:
    kVer += tempVer
    tempVer -= 2

kHor = 0
tempHor = m-1
while tempHor > 0:
    kHor += tempHor
    tempHor -= 2


print(kVer*(m+1)+kHor*(n+1)+kVer*kHor*2)
