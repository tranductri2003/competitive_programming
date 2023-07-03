
def available(current, target):
    current = bin(current)[2:]
    target = bin(target)[2:]
    current = '0'*(len(target)-len(current))+current
    for i in range(len(target)):
        if target[i] == '0' and current[i] == '1':
            return False
    else:
        return True


t = int(input())
for _ in range(t):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    current = 0
    for i in range(n):
        if a[i] > x:
            break
        if available(a[i], x):
            current = current | a[i]
        else:
            break

    for i in range(n):
        if b[i] > x:
            break
        if available(b[i], x):
            current = current | b[i]
        else:
            break

    for i in range(n):
        if c[i] > x:
            break
        if available(c[i], x):
            current = current | c[i]
        else:
            break
    if x == 0:
        print("Yes")
    else:
        if current == x:
            print("Yes")
        else:
            print("No")
