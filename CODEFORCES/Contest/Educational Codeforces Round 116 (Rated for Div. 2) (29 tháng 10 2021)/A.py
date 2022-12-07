testcase=int(input())

for i in range(0,testcase):
    s=input()
    n=len(s)
    nab=0
    nba=0
    for j in range(0,n-1):
        if s[j]=="a":
            if s[j+1]=="b":
                nab+=1
        else:
            if s[j+1]=="a":
                nba+=1
    if nab==nba:
        print(s)
    else:
        if nab>nba:
            print("b",end="")
            print(s[1:])
        if nab<nba:
            print("a",end="")
            print(s[1:])

                    

                


