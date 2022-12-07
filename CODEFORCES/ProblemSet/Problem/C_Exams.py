


#!Run time Error
# n=int(input())

# a={}

# for i in range(n):
#     b,a[b]=list(map(int,input().split()))

# temp=a.items()
# arranged=sorted(temp)

# res=-1
# for i in range(0,n):
#     if res<=arranged[i][1]:
#         res=arranged[i][1]
#     else:
#         res=arranged[i][0]
# print(res)



n=int(input())
data=[]
for _ in range(n):
    a,b=list(map(int,input().split()))
    data.append((a,b))
data.sort()

res=0
for num in data:
    if num[1]>=res:   #Vẫn còn hẹn lịch sắp tới nên chốt được
        res=num[1]
    else:
        res=num[0]    #Lịch đã qua nên phải lấy ngày xa hơn
print(res)
    