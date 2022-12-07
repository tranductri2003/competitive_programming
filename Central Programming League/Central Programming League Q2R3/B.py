
def mahoa(s):
    s = str(s)
    data = [s[0]]
    current = s[0]
    for i in range(1, len(s)):
        if s[i] != current:
            data.append(s[i])
            current = s[i]
    j = 0

    num = []
    stack = 0
    for i in range(len(s)):
        if s[i] == data[j]:
            stack += 1
        else:
            num.append(stack)
            stack = 1
            j += 1
    num.append(str(stack))

    res = ""
    for i in range(len(num)):
        res += str(num[i])+data[i]
    return res


n = int(input())  # So lan ma hoa
s = input()
for i in range(n):
    s = mahoa(s)
print(s)
