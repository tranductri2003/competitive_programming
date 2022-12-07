def binary_search(chuoinhatbien,giatricanxacdinhvitri,len):
    bottom=0
    top=len-1

    while bottom<=top:
        middle=(bottom+top)//2

        if chuoinhatbien[middle]==giatricanxacdinhvitri:
            break

    
        elif chuoinhatbien[middle]>giatricanxacdinhvitri:
            top=middle-1
        else:
            bottom=middle+1
    
    while chuoinhatbien[middle]>=giatricanxacdinhvitri:
        middle=middle-1
        if middle<0:
            break
    return middle+1
        

        
        


n=int(input())
chuoi=list(map(int, input().split()))
chuoi.sort()

ans=0
for i in range(0,n-2):
    for j in range(i+1,n-1):

        ans=ans+binary_search(chuoi[j+1:],chuoi[i]+chuoi[j],n-j-1)

print(ans)
        



