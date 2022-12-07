
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
#!      Filename: K_Mashmokh_and_ACM.py
#*      Folder: D:\Code\Python\Codeforces\ProblemSet\Topic Stream Mashup Dynamic Programming
#?      Author: TranDucTri2003
#TODO   CreatedAt: 08/09/2022 15:48:12
#? -----------------------------------------------------------------------------------------------------

#Chuối tốt nếu như b[i] được chia hết bởi b[i] : ví dụ 1, 3
#Cho n và k tìm chuỗi tốt dài k với các phần tử <=n

#! dp[i][j]: số chuỗi đẹp có độ dài là i và kết thúc là số j
#? Khi ta xét một chuỗi độ dài n, kết thúc bằng số k.
#? Nếu chuỗi n+1 kết thúc bằng x với x%k==0 thì sẽ được bổ sung thêm số cách bằng đúng dp[n][k]

#TODO Có thể tự hiểu là cũng viết lại y chang các chuỗi đẹp đó và thêm số x ở cuối cùng.

n,k=list(map(int,input().split()))
dp=[]
for i in range(k+1):
    dp.append([])
    for j in range(n+1):
        dp[i].append(0)

dp[0][1]=1  
for i in range(1,k+1):
    for j in range(1,n+1):
        for x in range(j,n+1,j):
            dp[i][x]=(dp[i][x]+dp[i-1][j])%(10**9+7)

res=0

for i in range(1,n+1):
    res+=dp[k][i]
print(res%(10**9+7))