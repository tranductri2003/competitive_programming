testcase=int(input())


for test in range(testcase):
    n,k=list(map(int,input().split()))
    hour=0
    done=1 
    abilitiy=1
    while done<n:
        done+=abilitiy
        hour+=1
        if abilitiy*2<= k:
            abilitiy*=2
        else:
            if (n-done)%k==0:
                hour+=(n-done)//k
            else:
                hour+=(n-done)//k+1
            break
    print(hour)

        