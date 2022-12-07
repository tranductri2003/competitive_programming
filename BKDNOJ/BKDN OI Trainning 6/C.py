import string

data = string.ascii_uppercase
s = input()

for i in range(len(s)):
    temp = s[i]
    pos = data.find(temp)
    pos = pos-3
    print(data[pos], end="")
