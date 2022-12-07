a=[0]*100
a[0]=1
a[1]=3
for i in range(2,100):
    a[i]=6*a[i-1]-9*a[i-2]
    if a[i]!=3**i:
        print('1')
