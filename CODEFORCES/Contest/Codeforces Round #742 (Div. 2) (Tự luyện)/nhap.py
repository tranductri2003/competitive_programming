for i in range(int(input())):
    s = '0' + input()
    print(s)
    print(s[0::2])
    print(s[1::2])
    print((int(s[0::2])+1)*(int(s[1::2])+1)-2)