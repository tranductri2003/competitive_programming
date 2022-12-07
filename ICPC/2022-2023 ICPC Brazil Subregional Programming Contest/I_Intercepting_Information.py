a = list(map(int, input().split()))
for num in a:
    if num != 0 and num != 1:
        print("F")
        break
else:
    print("S")
