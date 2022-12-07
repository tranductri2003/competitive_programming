testcase=int(input())
for test in range(testcase):
    n,a,b=list(map(int,input().split()))
    string=input()
    if b>=0:
        res=(a+b)*n
    else:

        string=list(string)
        string.insert(0,2)
        mangmoi=[]

        for i in range(1,n+1):
            if string[i]!=string[i-1]: 
                mangmoi.append(string[i])
        string.pop(0)
        so1=mangmoi.count('1')
        so0=mangmoi.count('0')
        if so0<=so1:
            string.append(2)
            res=0
            stack=0
            for i in range(n+1):
                if string[i]=='0':
                    stack+=1
                else:
                    if stack!=0:
                        res+=a*stack+b
                        stack=0
            num1=string.count('1')
            if num1!=0:
                res+=a*num1+b
        else:
            string.append(2)
            res=0
            stack=0
            for i in range(n+1):
                if string[i]=='1':
                    stack+=1
                else:
                    if stack!=0:
                        res+=a*stack+b
                        stack=0
            num0=string.count('0')
            if num0!=0:
                res+=a*num0+b
        
    print(res)