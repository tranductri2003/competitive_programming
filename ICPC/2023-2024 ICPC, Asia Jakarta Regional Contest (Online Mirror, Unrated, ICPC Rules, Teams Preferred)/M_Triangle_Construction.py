N = int(input())
a = list(map(int, input().split()))

temp1 = sum(a)//3

temp2 = min(temp1, sum(a)-max(a))
print(temp2)
