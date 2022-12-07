t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    temp=[]
    for num in a:
        
        if num%2==0:
            temp.append(num)
        else:
            temp.append(num+num%10)

            


    temp.sort()
    for i in range(len(temp)-1):
        dis=temp[i+1]-temp[i]

        conlai=dis-dis//20*20
        
        
        if temp[i]%10==0:
            if temp[i+1]>temp[i]:
                print("No")
                break
        elif temp[i]%10==2:
            if conlai==0 or conlai==2 or conlai==6 or conlai==14:
                pass
            else:
                print("No")
                break
        elif temp[i]%10==4:
            if conlai==0 or conlai==4 or conlai==12 or conlai==18:
                pass
            else:
                print("No")
                break    
        elif temp[i]%10==8:
            if conlai==0 or conlai==8 or conlai==14 or conlai==16:
                pass
            else:
                print("No")
                break 
        elif temp[i]%10==6:
            if conlai==0 or conlai==6 or conlai==8 or conlai==12:
                pass
            else:
                print("No")
                break 
    else:
        print("Yes")


# n=int(input())
# res=[n]
# for i in range(101):
#     res.append(res[-1]+res[-1]%10)
# print(*res)