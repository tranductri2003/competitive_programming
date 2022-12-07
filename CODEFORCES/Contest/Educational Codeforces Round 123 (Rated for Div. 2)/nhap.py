from re import S


n=int(input())

string=["0"]*n
while True:
    temp="".join(string)
    print (temp)
    i=n-1
    while i>-1 and string[i]=="1":
        i-=1
    string[i]="1"
    if i==-1:
        break
    for j in range(i+1,n):
        string[j]="0"

    