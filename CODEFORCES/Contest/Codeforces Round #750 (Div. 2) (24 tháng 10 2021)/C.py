testcase=int(input())

for test in range(0,testcase):
    n=int(input())
    a=input()

    if len(a)==1:
        print(0)
    else:
        i=0
        j=n-1

        stop=False
        while a[i]==a[j] and stop==False:
            i+=1
            j-=1
            if i>=j:
                print(0)
                stop=True


        if stop==False:

            temp1=a[i]
            temp2=a[j]
            i=0
            j=n-1
            count1=0
            stop1=False
            while i<j and stop1==False:
                if a[i]==a[j]:
                    i+=1
                    j-=1
                else:
                    if a[i]!=temp1 and a[j]!=temp1:
                        stop1=True
                        count1=10**9                
                    if a[i]==temp1:
                        i+=1
                        count1+=1
                    if a[j]==temp1:
                        j-=1
                        count1+=1


            i=0
            j=n-1
            count2=0
            stop2=False
            while i<j and stop2==False:
                if a[i]==a[j]:
                    i+=1
                    j-=1
                else:
                    if a[i]!=temp2 and a[j]!=temp2:
                        stop2=True
                        count2=10**9
                    if a[i]==temp2:
                        i+=1
                        count2+=1
                    if a[j]==temp2:
                        j-=1
                        count2+=1

            
            if stop1==True and stop2==True:
                print(-1)
            else:
                print(min(count1,count2))
        
