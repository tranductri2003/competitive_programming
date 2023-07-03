n = int(input())
a = list(map(int, input().split()))
must = n*(n+1)//2
if (sum(a)-must) % 2 == 0:
    print("CPU")
else:
    print("TUAN")
