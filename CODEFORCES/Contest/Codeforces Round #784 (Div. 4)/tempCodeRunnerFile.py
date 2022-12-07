t=int(input())
for _ in range(t):
    n=int(input())
    a=list(input())

    #Chạy từ phải sang trái và chạy từ trái sang phải
    leftToRight=True
    rightToLeft=True

    res1=["W"]*n
    res2=["W"]*n
    if n==1:
        print("NO")
    else:
            
        #Left to right
        i=0
        while i<=n-2:
            if i==n-2:
                if (a[i]=="W" and a[i+1]!="W") or (a[i+1]=="W" and a[i]!=res1[i]) or (a[i+1]==a[i]!="W"):
                    leftToRight=False
                    break
                else:
                    i+=1
            else:
                if res1[i]==a[i]:
                    i+=1
                    pass
                else:
                    if a[i]=="W":
                        leftToRight=False
                        break
                    else:
                        if res1[i]=="B":
                            res1[i]="R"
                            res1[i+1]="B"
                            i+=1
                        else:
                            res1[i]="B"
                            res1[i+1]="R"
                            i+=1
            
        #Right to left
        i=n-1
        while i>=1:
            if i==1:
                if (a[i]=="W" and a[i-1]!="W") or (a[i-1]=="W" and a[i]!=res2[i]) or (a[i-1]==a[i]!="W"):
                    rightToLeft=False
                    break
                else:
                    i-=1
            else:
                if res2[i]==a[i]:
                    i-=1
                    pass
                else:
                    if a[i]=="W":
                        rightToLeft=False
                        break
                    else:
                        if res2[i]=="B":
                            res2[i]="R"
                            res2[i-1]="B"
                            i-=1
                        else:
                            res2[i]="B"
                            res2[i-1]="R"
                            i-=1
        
        if leftToRight==rightToLeft==False:
            print("NO")
        else:
            print("YES")
                    
