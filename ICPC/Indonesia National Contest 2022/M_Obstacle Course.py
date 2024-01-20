N = int(input())
a = list(map(int,input().split()))
data = []
for i in range(0, N, 2):
    data.append(a[i])

check = [True]

nData = len(data)
for i in range(1, nData):
    if data[i] == data[i-1] or abs(data[i]-data[i-1])==2:
        check.append(True)
    else:
        check.append(False)

print(check)
i=0
res=2
while i<nData:
    if check[i] == True:
        start = i
        tempRes =0
        length=0
        while i<nData and check[i]==True:
            length+=1
            i+=1
        finish = i
        tempRes =(length)*2-1
        if (finish-1)*2+1!=N:
            tempRes+=1
        if start!=0:
            tempRes+=1
        res = max(res, tempRes)
        print("length: ",length, "tempRes: ",tempRes, "res: ",res)
    else:
        tempRes=1
        if i*2+1!=N:
            tempRes+=1
            # print('a')
        if i!=0:
            tempRes+=1
            # print('b')
        # print('tempRes: ',tempRes)
        res = max(res, tempRes)
        i+=1
print(res)