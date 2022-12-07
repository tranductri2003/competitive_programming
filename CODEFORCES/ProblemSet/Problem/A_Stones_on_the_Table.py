n=int(input())
s=input()

#Bất cứ 2 bi liền kề khác màu
res=0
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        res+=1
print(res)