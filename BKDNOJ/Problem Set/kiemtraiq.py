# https://bkdnoj.dut.udn.vn/public/practice_problem.php?id=DUT21B

matrix=[]
for i in range(0,4):
    matrix.append([])
    for j in range(0,4):
        matrix[i].append(0)
for i in range(0,4):
    a=str(input())
    for j in range(0,4):
        if a[j]=="#":
            matrix[i][j]=1


    
stop=False
for i in range(0,3):
    for j in range(0,3):
        color=matrix[i][j]+matrix[i][j+1]+matrix[i+1][j]+matrix[i+1][j+1]
        if color==1 or color==3 or color==0 or color==4:
            print("YES")
            stop=True
            break
    if stop==True:
        break
if stop==False:
    print("NO")