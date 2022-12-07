t = int(input())
for i in range(t):
    n = int(input())
    souocchan = 0
    for j in range(1, n+1):
        if n % j == 0:
            if j % 2 == 0:
                souocchan = souocchan+1
    print(souocchan)
