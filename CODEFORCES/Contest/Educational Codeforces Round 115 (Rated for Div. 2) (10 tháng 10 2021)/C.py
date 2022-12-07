
testcase=int(input())

for test in range(0,testcase):
    dictionary={}
    n=int(input())
    a=list(map(int,input().split()))
    for num in a:
        dictionary[num]=0
    for num in a:
        dictionary[num]+=1
    S=sum(a)
    k=S/n
    tonggiatricanxoa=k*2
    res=0
    for i in range(0,n):

        if tonggiatricanxoa-a[i] in dictionary:
            res+=dictionary[tonggiatricanxoa-a[i]]
            if a[i]==k:
                res-=1
    print(res//2)
