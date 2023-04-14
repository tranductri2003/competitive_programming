import sys
sys.stdin = open("hanya.in", "r")
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    am = False
    duong = False
    for num in a:
        if num > 0:
            duong = True
        elif num < 0:
            am = True

    if am == False and duong == False:
        print(0)
    elif am == True and duong == True:
        print(2)
    else:
        print(1)
