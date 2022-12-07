

from re import M


testcase = int(input())
for test in range(testcase):
    h,w=list(map(int,input().split()))
    
    matrix=[]
    for i in range(h):
        matrix.append([])
        for j in range(w):
            matrix[i].append(0)

    for i in range(0,h,2):
        if i==0 or i==h-1:
            for j in range(0,w,2):
                matrix[i][j]=1
        else:
            matrix[i][0]=1
            matrix[i][-1]=1

    if matrix[h-1][0]==0 and matrix[h-2][0]==1:
        for i in range(w):
            matrix[h-2][i]=0
        for i in range(0,w,2):
            matrix[h-1][i]=1
    for i in range(h):
        for j in range(w):
            matrix[i][j]=str(matrix[i][j])
        res="".join(matrix[i])
        print(res)
    print()