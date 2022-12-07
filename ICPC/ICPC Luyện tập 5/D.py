from collections import defaultdict
N, F, D = list(map(int, input().split()))

cowFood = defaultdict(list)
cowDrink = defaultdict(list)
for _ in range(1, N+1):
    a = list(map(int, input().split()))
    nFood = a[0]
    nDrink = a[1]
    cowFood[_] = a[2:2+nFood]
    cowDrink[_] = a[2+nFood:]
cowFood = dict(cowFood)
cowDrink = dict(cowDrink)
print(cowFood)
print(cowDrink)
