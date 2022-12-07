t=int(input())

for _ in range(t):
    n,k=list(map(int,input().split()))
    #Tổng số chẵn là số chẵn
    #Tổng số lẻ là số chẵn hoặc là số lẻ

    #Nếu n là số chẵn thì có thể chọn k số chẵn hoặc là k số lẻ
    #Nếu n là số lẻ thì chỉ có thể chọn k số lẻ

    #!N chẵn, k lẻ: chỉ có thể chọn k số chẵn
    #!N chẵn, k chẵn: có thể chọn k số chẵn hoặc là k số lẻ
    #!N lẻ, k chẵn: in NO  
    #N lẻ, k lẻ: chỉ có thể chọn k số lẻ

    if n%2==1 and k%2==0:
        print("NO")
    elif n%2==0 and k%2==1:
        if n>=2*k:
            print("YES")
            print("2 "*(k-1),end='')
            print(n-2*(k-1))
        else:
            print("NO")
    elif n%2==k%2==0:
        if n>=k:
            print("YES")
            print("1 "*(k-1),end='')
            print(n-(k-1))
        else:
            print("NO")
    elif n%2 == k%2==1:
        if n>=k:
            print("YES")
            print("1 "*(k-1),end='')
            print(n-(k-1))
        else:
            print("NO")       
    