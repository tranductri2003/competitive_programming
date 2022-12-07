t=int(input())
for _ in range(t):
    n0,n1,n2=list(map(int,input().split()))
    #n0: có 0 số 1 00
    #n1: có 1 số 1 01 10
    #n2: có 2 số 1 11

    #00 kết hợp với 00, 01
    #10 kết hợp với 11, 10
    #01 kết hợp với 10, 11
    #11 kết hợp với 10, 11

    if n1%2==1: #Sẽ đổi dấu
        if n2>= n0: 
            res=["1"]*(n2+1)
            for i in range(n1):
                if i%2==0:
                    res.append("0")
                else:
                    res.append("1")
            res+=["0"]*n0
        else: 
            res=["0"]*(n0+1)
            for i in range(n1):
                if i%2==0:
                    res.append("1")
                else:
                    res.append("0")            
            res+=["1"]*n2
    else: #Không đổi dấu
        if n2>=n0:
            res=["1"]*(n2+1)
            if n1>0:
                res.append("0") #Giờ số n1 trừ 1)
            res+=["0"]*n0
            for i in range(n1-1):
                if i%2==0:
                    res.append("1")
                else:
                    res.append("0") 
        else:
            res=["0"]*(n0+1)
            if n1>0:
                res.append("1")
            res+=["1"]*n2
            for i in range(n1-1):
                if i%2==0:
                    res.append("0")
                else:
                    res.append("1")
    res="".join(res)
    print(res)