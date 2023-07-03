
def check(temp, key):
    temp = bin(temp)[2:]
    key = bin(key)[2:]
    # print(temp, key)
    temp = '0'*(len(key)-len(temp))+temp
    # print(temp, key)
    for i in range(len(key)):
        if key[i] == '0' and temp[i] == '1':
            return False
    else:
        return True


t = int(input())
for _ in range(t):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    if x == 0:
        print("Yes")
    else:
        data = []
        i = j = k = 0
        while i < n or j < n or k < n:
            so1 = so2 = so3 = 10**9+5
            if i < n:
                so1 = a[i]
            if j < n:
                so2 = b[j]
            if k < n:
                so3 = c[k]
            if so1 == min(so1, so2, so3):
                data.append(so1)
                i += 1
            elif so2 == min(so1, so2, so3):
                data.append(so2)
                j += 1
            else:
                data.append(so3)
                k += 1
        temp = 0
        # print(data)
        for i in range(len(data)):
            if data[i] > x:
                print("No")
                break
            if check(data[i], x) == True:
                temp |= data[i]
                # print(x, 111, data[i])
                # print(i, data[i])
            else:
                print("No")
                break
            if temp > x:
                print("No")
                break
            if temp == x:
                print("Yes")
                break
        else:
            if temp == x:
                print("Yes")
            else:
                print("No")


# print(check(6, 1))
