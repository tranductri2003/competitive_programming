from random import randint


ques = []
ans = []
for _ in range(1):
    # l = randint(1, 1000)
    # r = randint(l, 10000)
    l = int(input())
    r = int(input())
    res = 0
    for i in range(l, r+1):
        temp = 1
        for j in range(len(str(i))):
            temp *= int(str(i)[j])
        res = max(res, temp)
    ques.append(l)
    ques.append(r)
    ans.append(res)

for num in ques:
    print(num)

print()
print()
print()
print()
print()
print()
print()
for num in ans:
    print(num)
