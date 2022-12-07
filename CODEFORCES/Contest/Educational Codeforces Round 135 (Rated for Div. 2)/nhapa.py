import heapq

n = int(input())
a = list(map(int, -input().split()))
b = list(map(int, -input().split()))
print(a)
print(b)


heapq.heapify(a)
print(a)
