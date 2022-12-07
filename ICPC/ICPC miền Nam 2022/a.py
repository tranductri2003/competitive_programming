from nhap import FastIO


x = int(input())
n = len(str(x))
data = []
for i in range(1, 10):
    data.append(int(str(i)*n))
data.append(int(str(1)*(n+1)))

for i in range(0, len(data)):
    if data[i] > x:
        print(data[i]-x)
        break
