from collections import defaultdict 
check = defaultdict(lambda: False)
res=0

t=int(input())
for _ in range(t):
    n=int(input())
    none = True
    for i in range(n):
        s = input()
        if "bie" in s and check[s]==False:
            print(s)
            check[s]=True
            none =False
    if none:
        print("Time to play Genshin Impact, Teacher Rice!")

        