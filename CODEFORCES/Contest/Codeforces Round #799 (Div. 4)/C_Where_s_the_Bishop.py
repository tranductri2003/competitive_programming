t=int(input())
for _ in range(t):
    space=input()
    matrix=[]
    for i in range(8):
        matrix.append([])
        for j in range(8):
            matrix[i].append('.')
    
    for i in range(8):
        s=input()
        for j in range(8):
            matrix[i][j]=s[j]
    
    
    for i in range(1,7):
        for j in range(1,7):
            if matrix[i][j]=="#" and matrix[i-1][j-1]=="#" and matrix[i-1][j+1] and matrix[i+1][j-1]=="#" and matrix[i+1][j+1]=="#":
                print(i+1,j+1)
                break