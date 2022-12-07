
t = int(input())
for _ in range(t):
    s1, s2 = input().split()
    if s1[-1] == s2[-1]:
        if s1[-1] == s2[-1] == "M":
            print("=")
        elif s1[-1] == s2[-1] == "L":
            so1 = s1.count("X")
            so2 = s2.count("X")
            if so1 == so2:
                print("=")
            elif so1 > so2:
                print(">")
            else:
                print("<")
        else:
            so1 = s1.count("X")
            so2 = s2.count("X")
            if so1 == so2:
                print("=")
            elif so1 < so2:
                print(">")
            else:
                print("<")
    else:
        if s1[-1] == "M":
            if s2[-1] == "L":
                print("<")
            else:
                print(">")
        elif s1[-1] == "S":
            print("<")
        else:
            print(">")
