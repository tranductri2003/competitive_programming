n = int(input())
a = list(map(int, input().split()))

left = [0]*n
right = [0]*n

current = a[0]
for i in range(n):
    if a[i]>current:
        current = a[i]
    left[i] = current

current = a[-1]
for i in range(n-1, -1, -1):
    if a[i]>current:
        current = a[i]
    right[i] = current
    
data=[]
temp=0
for i in range(1, n-1):
    if min(left[i], right[i])-a[i] ==0:
        data.append(temp)
        temp=0
    else:
        temp+=min(left[i], right[i])-a[i]

data.append(temp)
print(max(data))
    
    