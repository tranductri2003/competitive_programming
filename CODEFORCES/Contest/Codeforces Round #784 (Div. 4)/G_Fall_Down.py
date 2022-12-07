# An empty cell, denoted with '.'.
# A stone, denoted with '*'.
# An obstacle, denoted with the lowercase Latin letter 'o'.

t=int(input())
for _ in range(t):
    n,m=list(map(int,input().split()))
    matrix=[]
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append([])
    for i in range(n):
        s=input()
        for j in range(m):
            matrix[i][j]=s[j]


    for i in range(m):   #i chạy theo cột từ trái sang phải
        j=n-1     #j chạy theo hàng từ dưới lên trên
        while j>=0:
            if matrix[j][i]=="*":
                for k in range(j+1,n):   #k chạy theo hàng từ trên xuống dưới
                    if matrix[k][i]==".":
                        matrix[k][i]="*"
                        matrix[k-1][i]="."
                    else:
                        break
            j-=1
    for i in range(n):
        s="".join(matrix[i])
        print(s)
    print()     
