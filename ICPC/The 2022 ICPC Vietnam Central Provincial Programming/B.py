from random import randint
import string

model = string.ascii_uppercase
n = randint(1, 20)
s = ""
for _ in range(n):
    s += model[randint(0, min(5, len(s)))]
print(s)
# s = input()
testcase = 10
print(testcase)


datat = []
datares = []
# testcase = int(input())
for _ in range(testcase):
    t = randint(1, 5)
    print(t)
    datat.append(t)
    # t = int(input())
    temp = s[:t]

    res = 0
    for i in range(0, len(s)-len(temp)+1):
        if s[i:i+len(temp)] == temp:
            res += 1
    if s[:-t][::-1] != temp:
        res = 0
    if res == 0:
        datares.append("NO")
        print("NO")
    else:
        print("YES", res)
        datares.append(("YES", res))

print(s)
print(testcase)
for num in datat:
    print(num)
for num in datares:
    if num != 'NO':
        print(num[0], num[1])
    else:
        print(num)
