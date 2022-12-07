n = int(input())
res = ""
if n % 4 == 0:
    res = str(n//4-1)+"9"
elif n % 4 == 1:
    res = str(n//4)+"1"
elif n % 4 == 2:
    res = str(n//4)+"3"
elif n % 4 == 3:
    res = str(n//4)+"7"
print(int(res))
