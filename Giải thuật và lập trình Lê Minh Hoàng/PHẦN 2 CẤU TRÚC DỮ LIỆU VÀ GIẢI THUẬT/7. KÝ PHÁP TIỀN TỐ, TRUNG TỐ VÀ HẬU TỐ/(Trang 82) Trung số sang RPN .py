trungto=list(input().split())
n=len(trungto)
stack=list()
res=list()
def priority(a):
    if a=="*" or a=="/":
        return 2
    if a=="+" or a=="-":
        return 1
    if a=="(":
        return 0

for i in range(0,n):
    if trungto[i].isdigit()==True:
        res.append(trungto[i])
    elif trungto[i]=="(":
        stack.append("(")
    else:
        if trungto[i]==")":
            while stack[-1]!="(":
                res.append(stack[-1])
                stack.pop(-1)
            stack.pop(-1)
        else:
            if len(stack)!=0:
                while priority(trungto[i])<priority(stack[-1]):
                    res.append(stack[-1])
                    stack.pop(-1)
            stack.append(trungto[i])

for i in range(0,len(stack)):
    res.append(stack[i])

print("REFINED: ",end="")
print(*trungto)
print("RPN: ",end="")
print(*res)