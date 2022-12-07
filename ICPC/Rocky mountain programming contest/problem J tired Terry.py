n,p,d=list(map(int,input().split()))
"""
More precisely, for integers p and d, we say that Terry is tired at second i if from second i−p+1 to second i (inclusive) he has slept for less than d seconds.

Input
The first line of input contains three integers n (1≤n≤86400), the length of Terry’s sleep pattern, p (1≤p≤n), and d (1≤d≤p) as described above.

The second line of input contains a single string of length n which describes the period of time that is recorded. The ith such character is a W if Terry is awake at the ith second, or is a Z if Terry is asleep at the ith second.
"""

string=input()
string=string*2
temp=string[0:p]
sleep=0
res=0
for i in range(0,p):
    if temp[i]=="Z":
        sleep=sleep+1
for i in range(1,n+1):
    if string[i-1]=="Z":
        sleep-=1
    if string[i+p-1]=="Z":
        sleep+=1
    if sleep<d:
        res+=1
print(res)