
testcase=int(input())
for test in range(0,testcase):
    n=str(input())
    if int(n)%25==0:
        print(0)
    else:
        res=0
        vi1=vi2=vi3=vi4=False
        sosocanxoa1=999999
        sosocanxoa2=999999
        for i in range (len(n)-1,0,-1):

            if n[i]=="5":
                vitri1=i
                vi1=True
                for j in range (i-1,-1,-1):
                    if n[j]=="2" or n[j]=="7":
                        vitri2=j
                        vi2=True
                        break
                break
        if vi1==vi2==True:
            sosocanxoa1=len(n)-1-vitri2+1-2
        for i in range (len(n)-1,0,-1):
            if n[i]=="0":
                vitri3=i
                vi3=True
                for j in range (i-1,-1,-1):
                    if n[j]=="5" or n[j]=="0":
                        vitri4=j
                        vi4=True
                        break
                break
        if vi3==vi4==True:
            sosocanxoa2=len(n)-1-vitri4+1-2
        print(min(sosocanxoa1,sosocanxoa2))



        