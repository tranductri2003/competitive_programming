
t = int(input())
ok = ["Timur", "miurT", "Trumi", "mriTu"]
for _ in range(t):
    n = int(input())
    s = input()
    if n != 5:
        print("NO")
    else:
        if "T" in s and "i" in s and "m" in s and "u" in s and "r" in s:
            print("YES")
        else:
            print("NO")
