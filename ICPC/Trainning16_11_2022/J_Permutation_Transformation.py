

def recursion(a, level):
    if a == []:
        return 0
    giaTriMax = max(a)
    check[giaTriMax] = level
    recursion(a[:a.index(giaTriMax)], level+1)
    recursion(a[a.index(giaTriMax)+1:], level+1)


t = int(input())
for _ in range(t):
    n = int(input())
    check = [0]*(n+1)
    a = list(map(int, input().split()))
    # in ra depth d
    recursion(a, 0)
    # print(check)
    for num in a:
        print(check[num], end=" ")
    print()
