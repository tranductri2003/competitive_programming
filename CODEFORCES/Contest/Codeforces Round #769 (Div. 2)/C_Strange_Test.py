def bintonum(string):
    res=0
    s=0
    for i in range(len(string)-1,-1,-1):
        res+=int(string[i])*(2**s)
        s+=1
    return res
testcase=int(input())
for test in range(testcase):
    a,b=list(map(int,input().split()))
    soa=str(bin(a))[2:]
    sob=str(bin(b))[2:]


    vitri=0
    i=len(soa)-1
    j=len(sob)-1
    kiemtra=1
    stack=0
    while kiemtra<=len(soa):
        if soa[i]=="1" and sob[j]=="0":
            stack=kiemtra
            kiemtra+=1
            i-=1
            j-=1
        else:
            kiemtra+=1
            j-=1
            i-=1
    if stack==0:
        print(1)
    else:
        sotru="1"+stack*"0"
        sutrutru=bintonum(sotru)
        sobitri=bintonum(str(a))
        res=sutrutru-sobitri
        print(min(b-a,res))
