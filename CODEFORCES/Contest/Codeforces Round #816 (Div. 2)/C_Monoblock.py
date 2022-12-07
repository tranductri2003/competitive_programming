
n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
a.insert(0,10**10)
a.append(10**10)

ans=0
for i in range(1,n+1):
    if a[i]!=a[i-1]:
        k=i
    else:
        k=1
    g=n-i+1
    ans=ans+k*g



for i in range(m):
    pos,x=list(map(int,input().split()))
    if (a[pos]!=a[pos-1] and a[pos-1]==x):

        ans=ans-(pos*(n-pos+1));
        ans=ans+(n-pos+1);

    elif (a[pos]==a[pos-1] and a[pos-1]!=x):

        ans=ans+(pos*(n-pos+1));
        ans=ans-(n-pos+1);

    if (a[pos]!=a[pos+1] and a[pos+1]==x):

        ans=ans-((pos+1)*(n-pos));
        ans=ans+(n-pos);

    elif (a[pos]==a[pos+1] and a[pos+1]!=x):

        ans=ans+((pos+1)*(n-pos));
        ans=ans-(n-pos);

    a[pos]=x;
    print(ans)