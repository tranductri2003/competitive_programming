t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    # "Burenka" or "Tonya"


    if n % 2 == m % 2:
        print("Tonya")
    else:
        print("Burenka")
