def check_surrounding(matrix,n,m,i,j):
    if i-1>=0:
        if matrix[i][j]=="R":
            if matrix[i-1][j]=="R":
                return False
            else:
                if matrix[i-1][j]=="W":
                    pass
                else:
                    matrix[i-1][j]="W"
        elif matrix[i][j]=="W":
            if matrix[i-1][j]=="W":
                return False
            else:
                if matrix[i-1][j]=="R":
                    pass
                else:
                    matrix[i-1][j]="R"
        else:
            if matrix[i-1][j]=="R":
                matrix[i][j]="W"
            elif matrix[i-1][j]=="W":
                matrix[i][j]="R"
    if i+1<=n-1:
        if matrix[i][j]=="R":
            if matrix[i+1][j]=="R":
                return False
            else:
                if matrix[i+1][j]=="W":
                    pass
                else:
                    matrix[i+1][j]="W"
        elif matrix[i][j]=="W":
            if matrix[i+1][j]=="W":
                return False
            else:
                if matrix[i+1][j]=="R":
                    pass
                else:
                    matrix[i+1][j]="R"
        else:
            if matrix[i+1][j]=="R":
                matrix[i][j]="W"
            elif matrix[i+1][j]=="W":
                matrix[i][j]="R"
    if j-1>=0:
        if matrix[i][j]=="R":
            if matrix[i][j-1]=="R":
                return False
            else:
                if matrix[i][j-1]=="W":
                    pass
                else:
                    matrix[i][j-1]="W"
        elif matrix[i][j]=="W":
            if matrix[i][j-1]=="W":
                return False
            else:
                if matrix[i][j-1]=="R":
                    pass
                else:
                    matrix[i][j-1]="R"
        else:
            if matrix[i][j-1]=="R":
                matrix[i][j]="W"
            elif matrix[i][j-1]=="W":
                matrix[i][j]="R"
    if j+1<=m-1:
        if matrix[i][j]=="R":
            if matrix[i][j+1]=="R":
                return False
            else:
                if matrix[i][j+1]=="W":
                    pass
                else:
                    matrix[i][j+1]="W"
        elif matrix[i][j]=="W":
            if matrix[i][j+1]=="W":
                return False
            else:
                if matrix[i][j+1]=="R":
                    pass
                else:
                    matrix[i][j+1]="R"
        else:
            if matrix[i][j+1]=="R":
                matrix[i][j]="W"
            elif matrix[i][j+1]=="W":
                matrix[i][j]="R"
                          
testcase=int(input())
for test in range(testcase):
    n,m=list(map(int,input().split()))
    matrix=[]
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(".")
    for i in range(n):
        string=input()
        for j in range(m):
            matrix[i][j]=string[j]
    # for i in range(n):
    #     print(*matrix[i])
    for i in range(n):
        stop=False
        for j in range(m):
            sit=check_surrounding(matrix,n,m,i,j)
            if sit==False:
                print("NO")
                stop=True
                break
        if stop==True:
            break
    else:
        copy=[]
        for i in range(n):
            copy.append([])
            for j in range(m):
                copy[i].append([])
        for i in range(n):
            for j in range(m):
                copy[i][j]=matrix[i][j]
                
        for i in range(n):
            stop2=False
            for j in range(m):
                if matrix[i][j]==".":
                    matrix[i][j]="W"
                    if check_surrounding(matrix,n,m,i,j)!=False:
                        pass
                    else:
                        stop2=True
                        matrix[i][j]="."
                        break
                else:
                    sit=check_surrounding(matrix,n,m,i,j)
                    if sit==False:
                        stop2=True
                        break
            if stop2==True:
                break

        if stop2==True:
            for i in range(n):
                stop3=False
                for j in range(m):
                    if copy[i][j]==".":
                        copy[i][j]="R"
                        if check_surrounding(copy,n,m,i,j)!=False:
                            pass
                        else:
                            stop3=True
                            break
                    else:
                        sit=check_surrounding(copy,n,m,i,j)
                        if sit==False:
                            stop3=True
                            break
                            
        if stop2==True and stop3==True:
            print("NO")  
        else:
            print("YES")
            if stop2==False:
                for i in range(n):
                    for j in range(m):
                        print(matrix[i][j],end="")
                    print()
            else:
                for i in range(n):
                    for j in range(m):
                        print(copy[i][j],end="")
                    print()
                
        
                