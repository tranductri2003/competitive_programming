n=int(input())
n=str(n)

currentMax=int(n[0])
for i in range(1,len(n)):
    if int(n[i])>currentMax:
        currentMax=int(n[i])
print(currentMax)

# print(max(str(int(input()))))
