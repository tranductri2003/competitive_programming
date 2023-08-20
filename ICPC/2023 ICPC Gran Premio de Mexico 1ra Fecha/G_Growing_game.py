N=int(input())
check="0"

length=0
for i in range(N+1):
    check+="1"*(i+2)
    check+="0"*(i+2)
    length+=(i+2)*2
    if length>N:
        break

if check[N-1]=="0":
    print("Jane")
else:
    print("John")
    

