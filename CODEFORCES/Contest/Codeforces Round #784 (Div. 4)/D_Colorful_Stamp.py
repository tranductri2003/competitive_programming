t=int(input())
for _ in range(t):
    n=int(input())
    a=input().split('W')
    for space in a:
        b1= "R" in space
        b2= "B" in space
        if b1==b2:
            pass
        else:
            print("NO")
            break
        
    else:
        print("YES")
     
"""
for i in range(int(input())):
    n = int(input())
    l = input().split('W')
    bad = False
    for s in l:
        b1 = 'R' in s
        b2 = 'B' in s
        if (b1 ^ b2):
            bad = True
    print("NO" if bad else "YES")
"""