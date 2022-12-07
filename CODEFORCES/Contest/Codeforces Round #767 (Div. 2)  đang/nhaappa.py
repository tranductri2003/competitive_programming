# class Matrix:
#     "Đây là class matrix"
    
#     def __init__(self):
#         print ("Nhap n:")
#         self.n=int(input())
#         print ("Nhap m")
#         self.m=int(input())
#         self.matrix=[]
#         for i in range(self.n):
#             self.matrix.append([])
#             for j in range(self.m):
#                 self.matrix[i].append([0])
#         print("Moi ban nhap ma tran: ")
#         for i in range(self.n):
#             for j in range(self.m):
#                 print(f"{[i]}{[j]}= ",end="")
#                 self.matrix[i][j]=int(input())
#     def showMatrix(self):
#         print ("Ma tran cua ban la: ")
#         for i in range(self.n):
#             print(*self.matrix[i])

# matran=Matrix()
# print(matran.__doc__)
# matran.showMatrix()

class Matrix:
    "Đây là class matrix"
    
    def initMatrix(self,n):
        self.matrix=[]
        for i in range(n):
            self.matrix.append([])
            for j in range(n):
                self.matrix[i].append([0])
        print("Moi ban nhap ma tran: ")
        for i in range(n):
            for j in range(n):
                print(f"{[i]}{[j]}= ",end="")
                self.matrix[i][j]=int(input())

    def createMatrix(self,n):
        self.matrix=[]
        for i in range(n):
            self.matrix.append([])
            for j in range(n):
                self.matrix[i].append(0)
    
    def getElement(self,i,j):
        return self.matrix[i][j]
    
    def setElement(self,i,j,num):
        self.matrix[i][j] = num
        
    def showMatrix(self,n):
        print ("Ma tran cua ban la: ")
        for i in range(n):
            print(*self.matrix[i])
                
    def sumMatrix(self,matran1,matran2,n,mod):
        self.createMatrix(n)
        for i in range(n):
            for j in range(n):
                num1=matran1.getElement(i,j)
                num2=matran2.getElement(i,j)                
                self.setElement(i,j,(num1+num2)%mod)
                
    def multiplyMatrix(self,matran1,matran2,n,mod):
        self.createMatrix(n)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    current=self.getElement(i,j)
                    num1=matran1.getElement(i,k)
                    num2=matran2.getElement(k,j)
                    result=(current+num1*num2)%mod
                    self.setElement(i,j,result)
    
    def powerMatrix(self,matranres,matran,n,k,mod):
        if k==1:
            return matran
        Q=Matrix()        
        Q.powerMatrix(matranres,matran,n,k//2,mod)
        if k%2==0:
            return matranres.multiplyMatrix(Q,Q,n,mod)
        else:
            Q2=Matrix()
            Q2.multiplyMatrix(Q,Q,n,mod)
            return matranres.multiplyMatrix(Q2,matran,n,mod)
        

matran1=Matrix()
matran1.initMatrix(2)
matran1.showMatrix(2)
matran2=Matrix()
matran2.initMatrix(2)
matran2.showMatrix(2)

matran3=Matrix()
matran3.sumMatrix(matran1,matran2,2,1000000)
matran3.showMatrix(2)

matran4=Matrix()
matran4.multiplyMatrix(matran1,matran2,2,1000000)
matran4.showMatrix(2)

matran5=Matrix()

matran5.powerMatrix(matran5,matran1,2,2,1000000)
matran5.showMatrix()


        