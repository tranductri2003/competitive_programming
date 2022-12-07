songuoi=int(input())
chuoi=list(map(int,input().split()))

order=list()
order.append(1)
for i in range(0,songuoi-1):
    order.append(chuoi.index(i)+2)

for ng in order:
    print(ng, end=" ")
