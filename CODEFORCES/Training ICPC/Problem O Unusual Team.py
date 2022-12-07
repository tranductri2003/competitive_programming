testcase=int(input())

for i in range(0,testcase):
    a,b=list(map(int,input().split()))
    if a<b:
        print("WeWillEatYou")
    else:
        print("FunkyMonkeys")
