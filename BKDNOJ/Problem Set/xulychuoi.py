# https://bkdnoj.dut.udn.vn/public/practice_problem.php?id=Demo6A

s=input()
n=len(s)

res=[]
done=False
for i in range(n):
    if s[i]=="_" and done==False:
        res.append(s[i])
        done=True
    if s[i]!="_":
        res.append(s[i])
        done=False

for i in range(0,len(res)):
    if res[i]!="_":
        res[i]=res[i].lower()
        
if res[0]=="_":
    res.pop(0)
if res[-1]=="_":
    res.pop(-1)

for i in res:
    print(i,end="")

        