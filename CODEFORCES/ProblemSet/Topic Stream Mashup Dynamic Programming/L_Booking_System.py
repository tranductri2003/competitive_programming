
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
#!      Filename: L_Booking_System.py
#*      Folder: D:\Code\Python\Codeforces\ProblemSet\Topic Stream Mashup Dynamic Programming
#?      Author: TranDucTri2003
#TODO   CreatedAt: 08/09/2022 23:32:56
#? -----------------------------------------------------------------------------------------------------

#! Dòng đầu tiên chứa số request
#! n dòng tiếp theo chứa số người đặt bàn và số tiền nhận được
#! dòng tiếp theo ghi số bàn mà nhà hàng có
#! dòng cuối ghi số chỗ mỗi bàn

#? dòng đầu tiên output ghi số bàn accepted để số tiền nhận được là tối đa
#? các dòng tiếp theo ghi số thứ tự của yêu cầu được chấp nhận và số bàn phân công tương ứng





n=int(input())

groups=[]
for i in range(n):
    size,price=list(map(int,input().split()))
    groups.append([size,price,i+1])

m=int(input())
k=list(map(int,input().split()))


tables=[]
for i in range (m):
    tables.append([k[i],i+1])

groups.sort(key=lambda x:(-x[1],x[0]))    #!Không cần x[0]
tables.sort(key=lambda x:x[0])

# print(groups)
# print(tables)

ans=0
res=[]

for i in range(n):
    for j in range(m):
        if tables[j][0]>=groups[i][0]:
            ans+=groups[i][1]
            res.append([groups[i][2],tables[j][1]])
            tables[j][0]=-1   #! Làm cho bàn nớ mất khả năng đi phục vụ nữa
            break
        
        
# for i in range(n):
#     for j in range(m):
#         if tables[j][0]>=groups[i][0]:
#             ans+=groups[i][1]
#             res.append([groups[i][2],tables[j][1]])
#             tables[j][0]=-1
#             groups[i][0]=10**9


print(len(res),ans)
for num in res:
    print(num[0],num[1])
            


            
