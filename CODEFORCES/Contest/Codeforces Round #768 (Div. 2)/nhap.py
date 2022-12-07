# for i in range(0,1000000):
#     if i&(i+1)==8:
#         print(f"{i}&{(i+1)}={i&(i+1)}")

res=0
for i in range(4,-1,-2):
    res+=i&(i-1)
print(res)