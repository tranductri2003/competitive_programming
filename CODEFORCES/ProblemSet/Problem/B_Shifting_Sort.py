from collections import deque
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    # if a==sorted(a):
    #     print(0)
    # else:
    #     b=sorted(a)
    #     k=0
    #     l=[]
    #     r=[]
    #     d=[]
    #     for i in range(0,n):
    #         if a[i]==b[i]:
    #             pass
    #         else:
    #             for j in range(n-1,-1,-1):
    #                 if a[j]==b[i]:
    #                     index=j
    #                     break
    #             change=deque(a[i:index+1])
    #             l.append(i+1)
    #             r.append(index+1)
    #             d.append(index-i)
    #             change.rotate(-d[-1])
    #             a=a[:i]+list(change)+a[index+1:]
    #             k+=1
    #     print(k)
    #     for i in range(0,len(l)):
    #         print(l[i],r[i],d[i])
    b=sorted(a)
    if a==b:
        print(0)
    else:
        k=0
        l=[]
        r=[]
        d=[]
        for i in range(0,n):
            pos=i+a[i:].index(b[i])
            if pos==i:
                pass
            else:
                a=a[:i]+[a[pos]]+a[i:pos]+a[pos+1:]
                l.append(i+1)
                r.append(pos+1)
                d.append(pos-i)
                k+=1
        print(k)
        for i in range(len(l)):
            print(l[i],r[i],d[i])
                
            
