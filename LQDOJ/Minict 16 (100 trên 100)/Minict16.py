n=int(input())

for i in range(0,n):
    chuoi=input()
    if len(chuoi)>10:
        print(chuoi[0]+str(len(chuoi)-2)+chuoi[len(chuoi)-1])
    else:
        print(chuoi)