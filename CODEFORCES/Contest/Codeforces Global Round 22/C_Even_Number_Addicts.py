

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    odd = 0
    even = 0
    for num in a:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd % 2 == 1:
        if odd % 4 == 1:
            if even % 2 == 0:
                print("Bob")
            else:
                print("Alice")
        else:
            print("Alice")
    else:
        if odd % 4 == 0:
            print("Alice")
        else:
            print("Bob")
