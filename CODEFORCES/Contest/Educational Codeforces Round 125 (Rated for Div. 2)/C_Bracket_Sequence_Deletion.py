t=int(input())

for _ in range(t):
    n=int(input())
    s=input()
    
    i=0
    
    operation=0
    left=n
    
    soluongtrai=0
    soluongphai=0
    while i<n:
        if s[i]==")":
            for j in range(i+1,n):
                if s[j]==")":
                    i=j+1
                    operation+=1
                    break
            else:
                break
        else:
            soluongtrai=1
            soluongphai=0
            for j in range(i+1,n):
                if s[j]==")":
                    soluongphai+=1
                else:
                    soluongtrai+=1
                if soluongtrai==2:
                    i=j+1
                    operation+=1
                    break
                if soluongtrai==soluongphai:
                    i=j+1
                    operation+=1
                    break
            else:
                break
    left=n-i
    print(operation,left)
            
            

        