from sys import stdin
def input():
    
    return stdin.readline()
from collections import defaultdict
t=int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    s=input()
    
    data=[]
    for i in range(0,n,k):
        data.append(s[i:i+k])
    # print()
    # print()
    
    #Sẽ lần lượt xét hai cột ngoài cùng rồi đi dần vô trong
    #Phải chọn đươc 1 chữ chung để đổi chung cho tất cả 2 cột đó
    #res+= 2*(n//k)- tần xuất chữ xuất hiện nhiều nhất

    #Ví dụ
# hipp o poto
# mons t rose
# squi p peda
# liop h obia   

#Ở hai côt ngoài cùng: res=8-2=6
#Tiếp đến 2 cột bên trong: res+=8-3=6+5=11
#Tiếp đến 2 cột bên trong nữa: res=11+5=16
#Tiếp đến 2 cột bên trong nữa: 16+4=20
#Tiếp đến 2 cột bên trong nữa: 20+3=23
    res=0
    for i in range(k//2):
        check=defaultdict(lambda:0)
        for num in data:
            check[num[i]]+=1
            check[num[k-i-1]]+=1
        res+=2*(n//k)-max(check.values())
    if k%2==1:
        check=defaultdict(lambda:0)
        for num in data:
            check[num[k//2]]+=1
        res+=(n//k)-max(check.values())  
        # print(check)   
    print(res)
        

"""
from sys import stdin
def input():
    
    return stdin.readline()
from collections import defaultdict
t=int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    s=input()
    
    data=[]
    for i in range(0,n,k):
        data.append(s[i:i+k])
    # print()
    # print()
    
    #Sẽ lần lượt xét hai cột ngoài cùng rồi đi dần vô trong
    #Phải chọn đươc 1 chữ chung để đổi chung cho tất cả 2 cột đó
    #res+= 2*(n//k)- tần xuất chữ xuất hiện nhiều nhất

    #Ví dụ
# hipp o poto
# mons t rose
# squi p peda
# liop h obia   

#Ở hai côt ngoài cùng: res=8-2=6
#Tiếp đến 2 cột bên trong: res+=8-3=6+5=11
#Tiếp đến 2 cột bên trong nữa: res=11+5=16
#Tiếp đến 2 cột bên trong nữa: 16+4=20
#Tiếp đến 2 cột bên trong nữa: 20+3=23
    res=0
    for i in range(k//2):
        check=defaultdict(lambda:0)
        for num in data:
            check[num[i]]+=1
            check[num[k-i-1]]+=1
        res+=2*(n//k)-max(check.values())
    if k%2==1:
        check=defaultdict(lambda:0)
        for num in data:
            check[num[k//2]]+=1
        res+=(n//k)-max(check.values())  
        # print(check)   
    print(res)
        """