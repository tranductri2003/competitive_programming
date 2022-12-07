t=int(input())

for _ in range(t):
    s=input()
    left=int(s[0])+int(s[1])+int(s[2])
    right=int(s[3])+int(s[4])+int(s[5])
    if left==right:
        print("YES")
    else:
        print("NO")