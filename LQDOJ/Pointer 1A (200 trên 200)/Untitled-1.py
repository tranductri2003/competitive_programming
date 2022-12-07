import math

x,y=list(map(float,input().split()))

tu=math.sqrt(y**2-x**2)
mau=y/x+1

r=tu/mau

Stron=math.pi*r**2



Scatlat=(math.acos(x/y)/(2*math.pi))*Stron



Stamgianho=1/2*r*math.sqrt((r*y/x)**2-r**2)
Stim=Stamgianho-Scatlat

print(Stim)