testcase=int(input())
for test in range(testcase):
    n=int(input())
    string=input()
    vitri=-1
    for i in range(0,n-1):
        if (string[i]=="?" and string[i+1]!="?") or(string[i]!="?" and string[i+1]=="?"): 
            vitri=i
            break

    if vitri!=-1:
        string=list(string)
        for i in range(vitri,-1,-1):
            if string[i]=="?":
                if string[i+1]=="R":
                    string[i]="B"
                else:
                    string[i]="R"
        if vitri<=n-2:
            for i in range(vitri+1,n):
                if string[i]=="?":
                    if string[i-1]=="R":
                        string[i]="B"
                    else:
                        string[i]="R"
    else:
        
        if string.find("?")==-1:
            string=list(string)
        else:
            string=list(string)
            for i in range(0,n):
                if i%2==0:
                    string[i]="R"
                else:
                    string[i]="B"
    for num in string:
        print(num,end="")          
    print(" ")
            
                
