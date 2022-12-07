
#? -----------------------------------------------------------------------------------------------------
#?　　　　　　　　　　　 ∧＿∧
#?　　　　　 ∧＿∧ 　 （´<_｀ ）　     
#?　　　　 （ ´_ゝ`）　/　 ⌒i        
#?　　　　／　　　＼　 　  |　|       
#?　　　 /　　 /￣￣￣￣/　|　 |
#?　 ＿_(__ﾆつ/　    ＿/ .| .|＿＿＿＿
#?　 　　　＼/＿＿＿＿/　（u　⊃
#?
#?		 /\_/\
#?		(= ._.)
#?		/ >WA \>AC
#?
#       WELCOME TO MY CODING SPACE
#!      Filename: F_Almost_Identity_Permutations.py
#*      Folder: D:\Code\Python\Codeforces\ProblemSet\Topic Stream Mashup Dynamic Programming
#?      Author: TranDucTri2003
#TODO   CreatedAt: 08/08/2022 22:39:29
#? -----------------------------------------------------------------------------------------------------



# from itertools import permutations

# def show(matrix):
#     for i in range(0,n+1):
#         for j in range(0,k+1):
#             # if j>i:
#             #     print("   X",end=" ")
#             # else:
#                 print("{:4}".format(matrix[i][j]),end=" ")
#         print()
        

# def solve(n,k):
#     res=0
#     a=list(permutations(range(1,n+1)))
#     for num in a:
#         check=0
#         for i in  range (n):
#             if num[i]==i+1:
#                 check+=1
#         if check>=n-k:
#             res+=1
#     return res
    
    
# n,k=list(map(int,input().split()))
# dp=[]
# for i in range(n+1):
#     dp.append([])
#     for j in range(k+1):
#         dp[i].append(solve(i,j))

# show(dp)

#? https://www.vedantu.com/question-answer/explain-derangements-write-the-formula-and-give-class-11-maths-cbse-5f91273cf689aa42cf30898b
#? https://brilliant.org/wiki/derangements/


# Derangements are arrangements of some number of objects into positions such that no object goes to its specified position. In the language of permutations, a derangement is a permutation \sigmaσ of nn elements with no fixed point; that is, \sigma(i) \ne iσ(i) 
# 
# ​
#  =i for all i \in \{1,2,\ldots,n\}i∈{1,2,…,n}.

# Let a, b, c, \ldots, na,b,c,…,n be nn distinct objects with their respective containers A, B, C, \ldots, N,A,B,C,…,N, and suppose aa goes into B.B. Then it gives rise to the following two cases:

# Case 1: When bb goes to A:A:
# Leaving out aa and b,b, there are derangements for n-2n−2 objects: D(n-2).D(n−2).

# Case 2: When bb goes to any other container:
# Leaving out a,a, the number of these is the same as the number of derangements of n-1n−1 objects ((including b): D(n-1).b):D(n−1).
# ((If cc goes to BB in the derangement of n-1n−1 objects, this corresponds to the derangement of nn objects where cc goes to AA and aa goes to B.)B.)

# Thus, the total is D(n-1)+D(n-2).D(n−1)+D(n−2).

# But the original assumption was that aa goes to BB. There are n-1n−1 choices for BB, so

# D(n)=(n-1)\big(D(n-1)+D(n-2)\big). \ _\square
# D(n)=(n−1)(D(n−1)+D(n−2)).


# The first line contains two integers n and k (4 ≤ n ≤ 1000, 1 ≤ k ≤ 4).
# Cho n và k: tìm số hoán vị sao cho có nhiều nhất k vị trí với p[i]!=i
#? Dearrangement là số cách sắp xếp sao cho p[i]!=i với mọi i
#? D[n]=(n-1)*(D[n-1]+D[n-2])


#TODO: D[]=[0,1,2,9,44,265,1854,14833,133496,...]
import math
n,k=list(map(int,input().split()))
res=0
if k==1: #có nhiều nhất một vị trí sai số là không thể
    pass
if k>=2: #Chọn ra một cặp gồm 2 số và đảo vị trí 2 số đó
    res+=1*math.comb(n,2)   #1 vì D[2]=1
if k>=3:
    res+=2*math.comb(n,3)   #2 vì D[3]=2   . 1 2 3 -> 2,1,3; 3,1,2
if k>=4:
    res+=9*math.comb(n,4) #9 vì D[4]=9. Mỗi khi chọn 1 cặp 4 số thì có tới 9 lần tận dụng để biến đổi sao cho 4 số đó p[i]!=i

res+=1  #chuỗi 1->n
print(res)






