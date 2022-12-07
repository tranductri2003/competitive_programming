
import sys
sys.stdin=open("building.in","r")
sys.stdout=open("building.out","w")
n=int(input())

string="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(2,n,n)
start=0
end=n
chuoi=string[0:n]
for i in range(n):
    for j in range(n):
        print(string[i],end="")
    print()
print()

for i in range(n):
    print(chuoi)




