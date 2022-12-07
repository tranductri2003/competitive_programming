testcase=int(input())

for i in range(0,testcase):
    chuoi=input()
    n=len(chuoi)
    tuphanbiet=chuoi.split(" ")
    limit=0
    for tu in tuphanbiet:
        limit=max(limit,len(tu))

    for i in range(2,n//limit+2):
        if (n-i+1)%i==0:
            a=0
            for j in range(1,i):
                
                if chuoi[(n-i+1)//i*j+a]!=" ":
                    break
                a=a+1
            else:
                print("YES")
                break
    else:
        print("NO")
    

