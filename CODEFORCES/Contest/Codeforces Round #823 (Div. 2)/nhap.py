a = 0
b = 0
t = int(input())
for _ in range(t):
    x, y = list(map(int, input().split()))
    if x > y:
        a += 1
    elif x < y:
        b += 1

if a > b:
    print("Mishka")
elif a < b:
    print("Chris")
else:
    print("Friendship is magic!^^")
