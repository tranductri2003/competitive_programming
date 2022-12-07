RPN=list(input().split())
n=len(RPN)
stack=list()
toantu=["+","-","*","/"]


for i in range(0,n):
    if RPN[i] in toantu:
        if RPN[i]=="+":
            res=int(stack[-2])+int(stack[-1])
        if RPN[i]=="-":
            res=int(stack[-2])-int(stack[-1])
        if RPN[i]=="*":
            res=int(stack[-2])*int(stack[-1])
        if RPN[i]=="/":
            res=int(stack[-2])/int(stack[-1])
        stack.pop(-1)
        stack.pop(-1)
        stack.append(res)
    else:
        stack.append(RPN[i])
print(stack[-1])