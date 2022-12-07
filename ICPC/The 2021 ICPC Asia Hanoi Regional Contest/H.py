t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        x, y = list(map(int, input().split()))
    winner = 1
    while n >= 2:
        n -= 2
        winner = 1-winner
    if winner == 0:
        print("Hoang")
    else:
        print("Vuong")
