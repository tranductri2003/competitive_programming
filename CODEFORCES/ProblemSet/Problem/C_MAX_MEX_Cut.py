testcase=int(input())
for test in range(testcase):
    n=int(input())
    string1=input()
    string2=input()
    
    i=0
    res=0
    while i<n:
        if string1[i]=="0" and string2[i]=="1" or string2[i]=="0" and string1[i]=="1":
            res+=2
            i+=1
        elif string1[i]=="0" and string2[i]=="0":
            if i<n-1:
                if string1[i+1]=="1" and string2[i+1]=="1":
                    res+=2
                    i+=2
                else:
                    res+=1
                    i+=1
            else:
                res+=1
                i+=1
        else:  #Deu bang 1
            if i<n-1:
                if string1[i+1]=="0" and string2[i+1]=="0":
                    res+=2
                    i+=2
                else:
                    i+=1
            else:
                i+=1
    print(res)
            