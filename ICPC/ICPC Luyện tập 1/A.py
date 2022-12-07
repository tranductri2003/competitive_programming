n = int(input())
s = input()
s = s.lower()
vitridausao = s.index('*')
truoc = s[:vitridausao]
dodaitruoc = len(truoc)
sau = s[vitridausao+1:]
dodaisau = len(sau)


data = []
for i in range(n):
    temp = input()
    temp = temp.lower()

    if len(s)-len(temp) > 1:
        print("NO")
    else:
        if temp[:dodaitruoc] == truoc and temp[len(temp)-dodaisau:] == sau:
            print("YES")
        else:
            print("NO")
