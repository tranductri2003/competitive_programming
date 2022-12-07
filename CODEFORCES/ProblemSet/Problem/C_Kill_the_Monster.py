from math import ceil


testcase=int(input())
for test in range(testcase):
    hc,dc=list(map(int,input().split()))
    hm,dm=list(map(int,input().split()))
    k,w,a=list(map(int,input().split()))
    #k: xu
    #moi xu co the tang w damge
    #moi xu co the tang a mau
    #dc/hm va dm/hc
    for i in range(0,k+1):
        temp1=ceil((hc+i*a)/dm)
        temp2=hm/(dc+(k-i)*w)
        if temp1>=temp2:
            print("YES")
            break
 
    else:
        print("NO")
                    