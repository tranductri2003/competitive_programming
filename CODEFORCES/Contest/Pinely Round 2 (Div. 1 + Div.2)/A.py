t=int(input())
for _ in range(t):
    n,a,q= list(map(int,input().split()))
    s=input()
    lack = n-a
    duong = s.count('+')
    am = s.count('-')
    
    best = a+duong
    worst = a
    temp=a
    for i in range(q):
        if s[i] =="+":
            temp+=1
        else:
            temp-=1
        worst = max(worst, temp)

    # print(best,worst)
    if worst >=n:
        print("YES")
    elif best >= n:
        print("MAYBE")
    else:
        print("NO")