testcase=int(input())
for test in range(testcase):
    n,k=list(map(int,input().split()))
    
#Khoang cach bang nhau
    if k==1:
        print("YES")
        for i in range(1,n+1):
            print(i)
    else:
        if n%2==0:
            matrix=[]
            for i in range(n):
                matrix.append([])
                for j in range(k):
                    matrix[i].append(0)
            temp=1
            for j in range(0,k):
                for i in range(n):
                    matrix[i][j]=temp
                    temp+=1
            print("YES")
            for i in range(n):
                print(*matrix[i])
        else:
            print("NO")