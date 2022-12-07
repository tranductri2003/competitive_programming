def showMatrix(matrix):
    for i in range(3):
        print(matrix[i])

def check(dp):
    if dp[0][0]=="X" and dp[1][1]=="X" and dp[2][2]=="X":
        return "the first player won"
    if dp[0][0]=="0" and dp[1][1]=="0" and dp[2][2]=="0":
        return "the second player won"
    if dp[0][2]=="X" and dp[1][1]=="X" and dp[2][0]=="X": 
        return "the first player won"
    if dp[0][2]=="0" and dp[1][1]=="0" and dp[2][0]=="0": 
        return "the second player won"    
    
    if dp[0][0]=="X" and dp[0][1]=="X" and dp[0][2]=="X": 
        return "the first player won"  
    if dp[1][0]=="X" and dp[1][1]=="X" and dp[1][2]=="X": 
        return "the first player won" 
    if dp[2][0]=="X" and dp[2][1]=="X" and dp[2][2]=="X": 
        return "the first player won"   
    if dp[0][0]=="0" and dp[0][1]=="0" and dp[0][2]=="0": 
        return "the second player won"  
    if dp[1][0]=="0" and dp[1][1]=="0" and dp[1][2]=="0": 
        return "the second player won" 
    if dp[2][0]=="0" and dp[2][1]=="0" and dp[2][2]=="0": 
        return "the second player won"   
    
    if dp[0][0]=="X" and dp[1][0]=="X" and dp[2][0]=="X": 
        return "the first player won"
    if dp[0][1]=="X" and dp[1][1]=="X" and dp[2][1]=="X": 
        return "the first player won"   
    if dp[0][2]=="X" and dp[1][2]=="X" and dp[2][2]=="X": 
        return "the first player won"      
    if dp[0][0]=="0" and dp[1][0]=="0" and dp[2][0]=="0": 
        return "the second player won"
    if dp[0][1]=="0" and dp[1][1]=="0" and dp[2][1]=="0": 
        return "the second player won"   
    if dp[0][2]=="0" and dp[1][2]=="0" and dp[2][2]=="0": 
        return "the second player won"     
    else:
        return False
for _ in range(int(input())):
    matrix=[]
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(0)
            
    nguoi1=0
    nguoi2=0

    for i in range(3):
        s=input()
        for j in range(3):
            if s[j]=="X":
                nguoi1+=1
            if s[j]=="0":
                nguoi2+=1
            matrix[i][j]=s[j]

    if abs(nguoi1-nguoi2)>1:
        print('illegal')
    else:
        if check(matrix)!=False:
            print(check(matrix))
        else:
            if nguoi1+nguoi2==9:
                print('draw')
            else:
                if nguoi1==nguoi2:
                    print('first')
                else:
                    print('second')


    