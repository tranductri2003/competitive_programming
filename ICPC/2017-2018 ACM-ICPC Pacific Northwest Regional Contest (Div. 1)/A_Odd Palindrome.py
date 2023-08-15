s=input()
n=len(s)
for i in range(0,n-1):
    if s[i]==s[i+1]:
        print("Or not.")
        break
else:
    print("Odd.")