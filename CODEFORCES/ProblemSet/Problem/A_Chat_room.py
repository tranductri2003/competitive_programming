# s=input()
# checkh=0
# checke=0
# checkl1=0
# checkl2=0
# checko=0
# for i in range(len(s)):
#     if s[i]=="h":
#         checkh=1
#     if s[i]=="e" and checkh==1:
#         checke=1
        
#     if s[i]=="l":
#         if checkh==1 and checke==1 and checkl1==1:
#             checkl2=1
#         elif checkh==1 and checke==1:
#             checkl1=1

#     if s[i]=="o" and checkh==1 and checke==1 and checkl1==1 and checkl2==1:
#         checko=1

# if checkh==1 and checke==1 and checkl1==1 and checkl2==1 and checko==1:
#     print("YES")
# else:
#     print("NO")

key='hello'
j=0
s=input()
for i in range(len(s)):
    if s[i]==key[j]:
        j+=1
    
    if j==5:
        break

if j<5:
    print("NO")
else:
    print("YES")
        