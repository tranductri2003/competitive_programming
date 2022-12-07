testcase=int(input())
for test in range(testcase):
    string=input()
    newstring=[string[0]]
    for i in range(1,len(string)):
        if string[i]!=string[i-1]:
            newstring.append(string[i])
            
    res=0
    for num in newstring: 
        if num=='0':
            res+=1
    print(min(res,2))
    