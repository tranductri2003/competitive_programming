def tohop(a,b):   #Tổ hợp chập a của b nên a phải nhỏ hơn b
    if a==0 or a==b:
        return 1
    if a==1:
        return b
    return tohop(a-1,b-1)+tohop(a,b-1)

testcase=int(input())
n=0
while n<testcase:
    length,change=map(int,input().split()) #length lớn hơn change
    print(2*tohop(change,length-1)%(10**9+7))
    n=n+1