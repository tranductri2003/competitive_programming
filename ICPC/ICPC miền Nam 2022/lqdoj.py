x = int(input())
n = len(str(x))
data = []
# 123
# 111 222 333 999

for i in range(1, 10):
    data.append(int(str(i)*n))
data.append(int('1'*(n+1)))

for i in range(len(data)):
    if data[i] > x:
        print(data[i]-x)
        break
