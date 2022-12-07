n=str(input())
sum=0
max=0
for i in range(0,len(n)):
    sum=sum+int(n[i])


if "0" not in n or sum%3!=0:
        print("-1")
else:
    chuoi=list(n)
    chuoi.sort(reverse=True)
    for num in chuoi:
        print(num, end="")