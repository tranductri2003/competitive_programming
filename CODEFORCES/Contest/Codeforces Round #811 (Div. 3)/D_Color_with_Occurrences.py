from collections import defaultdict

q=int(input())
for _ in range(q):
    s=input()
    lenS=len(s)
    check=defaultdict(lambda:False)
    
    stt=defaultdict(lambda:-1)
    
    n=int(input())
    doDaiMax=0
    for l in range(n):
        sub=input()
        check[sub]=True
        stt[sub]=l+1
        doDaiMax=max(doDaiMax,len(sub))
    
    res=0
    start=0
    pre=0
    
    ans=[]
    while True:
        doDaiHienTai=doDaiMax
        while True:
            if start+doDaiHienTai>lenS:
                doDaiHienTai-=1
            else:
                temp=s[start:start+doDaiHienTai]
                if check[temp]==True:
                    ans.append((stt[temp],start+1))
                    pre=start
                    start+=doDaiHienTai
                    res+=1
                    break
                else:
                    doDaiHienTai-=1
            if doDaiHienTai==0:
                start-=1
                break
        if start==pre or start<0:
            print(-1)
            break
        if start==lenS:
            print(res)
            for num in ans:
                print(num[0],num[1])
            break



