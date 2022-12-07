n=int(input())
thutuyeucau=list(map(int,input().split()))
j=1
time=0
stack=list()
solution=list()
for i in range(0,n):
    if len(stack)>0 and thutuyeucau[i]==stack[0]:        
        time+=1
        solution.append("B->C")
        stack.pop(0)
    else:
        while j<=n:
            if thutuyeucau[i]==j:
                time+=1
                j+=1
                solution.append("A->C")
                break
            else:
                stack.append(j)
                stack=stack[::-1]    #Nếu xóa dòng này sẽ ra dạng FIFO. Bởi vì nó không lật ngược mảng nữa
                solution.append("A->B")
                j+=1

if time==n:
    print("YES")
    for i in solution:
        print(i)
else:
    print("NO")