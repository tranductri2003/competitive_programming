
fib=[0]*100001
fib[1]=1
fib[2]=1

for i in range(3,100001):
    fib[i]=fib[i-1]+fib[i-2]

print(fib[100000])

first=1
second=1

for i in range(3,100001):
    second=second+first
    first=second-first

print(second)