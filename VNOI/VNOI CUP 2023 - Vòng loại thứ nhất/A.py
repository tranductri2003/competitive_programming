t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    for i in range(n):
        first = i+1
        second = p[i]
        third = p[second-1]
        fourth = p[third-1]

        if first != second and second != third and third != fourth and fourth == first:
            print("<3")
            break
    else:
        print("</3")
