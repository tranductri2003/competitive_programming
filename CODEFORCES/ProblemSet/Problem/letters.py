n=int(input())
a=input()
         
         
"""
• nếu s0 = ‘a’ và sn−1 = ‘a’, kết quả là 0
• nếu s0 = ‘a’ và sn−1 = ‘b’, kết quả là 1
• nếu s0 = ‘a’ và sn−1 = ‘?’, kết quả là 1
• nếu s0 = ‘b’ và sn−1 = ‘a’, kết quả là -1
• nếu s0 = ‘b’ và sn−1 = ‘b’, kết quả là 0
• nếu s0 = ‘b’ và sn−1 = ‘?’, kết quả là 0
"""
      
    
if a[0]=="a" and a[-1]=="a":
    res=0
elif a[0]=="a" and a[-1]=="b":
    res=1
elif a[0]=="a" and a[-1]=="?":
    res=1
elif a[0]=="b" and a[-1]=="a":
    res=-1
elif a[0]=="b" and a[-1]=="b":
    res=0
elif a[0]=="b" and a[-1]=="?":
    res=0
print(res)


"""
n=int(input())
a=list(input())

if "?" not in a:
    res=0
    for i in range(0,n-1):
        if a[i]=="a" and a[i+1]=="b":
            res+=1
        elif a[i]=="b" and a[i+1]=="a":
            res-=1
    print(res)
else:
    if "a" not in a and "b" not in a: 
        if n>=2:
            print(1)
        else:
            print(0)
    elif "a" not in a:   #Chỉ có b và dấu hỏi
        if a[0]=="?":
            print(1)
        else:
            print(0)
    elif "b" not in a: # Chỉ có a và dấu hỏi
        if a[-1]=="?":
            print(1)
        else:
            print(0)

    else:   #Có cả a, b và dấu hỏi
        for i in range(n-1,-1,-1):  #a cuối cùng
            if a[i]=="a":
                vitria=i
                break
        for i in range(0,n):    #b đầu tiên
            if a[i]=="b":
                vitrib=i
                break
            
     
        if vitria<vitrib:
            print(1)
        else:
            check1=False
            check2=False
            check3=False
            for i in range(vitrib,vitria):
                if a[i]=="?":
                    check2=True 
                    break
            if "?" not in a[0:vitrib] and "a" not in a[0:vitrib]:
                check1=True
            if "?" not in a[vitria:] and "b" not in a[vitria:]:
                check3=True
            
            if check1==False and check3==False:  #Có đầu cuối để bung sức
                print(1)
            else:
                if check1==True and check3==True:  #Đều không có
                    print(-1)
                else:
                    print(0)
                
                
        
        # for i in range(0,vitrib):
        #     if a[i] =="?": 
        #         a[i]="a"
        
        # for i in range(vitria,n):
        #     if a[i]=="?": 
        #         a[i]="b"

        # res=0
        # for i in range(0,n-1):
        #     if a[i]=="a" and a[i+1]=="b":
        #         res+=1
        #     elif a[i]=="b" and a[i+1]=="a":
        #         res-=1
        # print(res)

"""