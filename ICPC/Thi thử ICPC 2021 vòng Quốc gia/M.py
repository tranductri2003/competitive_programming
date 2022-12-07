for i in range(int(input())):
    n = int(input())
    if n % 2 == 1:
        print(-1)
        continue
    for j in range(1,int(n**0.5)):
        if n % (j*(j+1)) == 0:
            print(j, end=' ')
    print()