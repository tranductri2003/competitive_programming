#https://bkdnoj.dut.udn.vn/public/practice_problem.php?id=FC104_MATRIX

matrix=[]

for i in range(0,5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(0)

x=0
y=0
for i in range(0,5):
    a=list(map(int,input().split()))
    for j in range(0,5):
        if a[j]==1:
            x=i
            y=j
        matrix[i][j]=a[j]

res=abs(x-2)+abs(y-2)
print(res)