n=int(input())
thutuyeucau=list(map(int,input().split()))
j=1
time=0
queue=list()
solution=list()
for i in range(0,n):
    if len(queue)>0 and thutuyeucau[i]==queue[0]:        
        time+=1
        solution.append("B->C")
        queue.pop(0)
    else:
        while j<=n:
            if thutuyeucau[i]==j:
                time+=1
                j+=1
                solution.append("A->C")
                break
            else:
                queue.append(j)
                solution.append("A->B")
                j+=1

if time==n:
    print("YES")
    for i in solution:
        print(i)
else:
    print("NO")