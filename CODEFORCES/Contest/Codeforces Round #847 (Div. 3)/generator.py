t, n = 1, 2 * 10 ** 5
mask = (1 << 17) - 1
fill = int((1 << 15) * 1.3 + 1)
arr = []
arr += [mask + 2] * 2
x = 6
for i in range(1, fill):
    arr += [x] + [x]
    x = x * 5 + 1
    x = x & mask

arr += [1] * (n - len(arr))
s = " ".join(map(str, arr))


file = open("test.txt", "w")
print(t)
file.write(str(t)+"\n")
file.write(str(n)+"\n")
file.write(s)
for i in range(t):
    print(n)
    print(s)
