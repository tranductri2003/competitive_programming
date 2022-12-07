n,m=list(map(int,input().split()))

#n: số thẻ có số 0
#m: số thẻ có số 1

#Không có 2 thẻ có số 0 liên tiếp
#Không có 3 thẻ có số 1 liên Tiếp


if m>(n-1)*2+4:
    print(-1)
elif n>m+1:
    print(-1)
else: 
    #Trường hợp 1 số 0 và 1 số 1 đan xen nhau
    if m==n+1:
        res="10"*n+"1"
    elif m==n:
        res="10"*n
    elif m==n-1:
        res="01"*m+"0"
    
    #Đến lúc có 2 số 1 chen giữa các số 0
    else:
        succhuatoidakhoangtrongogiua=(n-1)*2
        if m<=succhuatoidakhoangtrongogiua:  #Chỉ cần số 2 lần số 1 ở trong là đủ rồi
            solanthemso1=m-(n-1)
            res=""
            res+="011"*(solanthemso1)
            res+="01"*(m-solanthemso1*2)
            res+="0"
        else: 
            #Cần thêm cả số 1 ở bên ngoài
            res="011"*(n-1)
            res+="0"
            
            so1bonus=m-res.count("1")
            if so1bonus==1 or so1bonus==2:
                res="1"*so1bonus+res
            elif so1bonus==3:
                res="11"+res+"1"
            else:
                res="11"+res+"11" 
    print(res)
