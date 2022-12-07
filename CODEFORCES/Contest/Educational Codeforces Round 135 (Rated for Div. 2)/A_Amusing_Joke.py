a = input()
b = input()
c = input()

temp = a+b
if sorted(temp) == sorted(c):
    print("YES")
else:
    print("NO")
