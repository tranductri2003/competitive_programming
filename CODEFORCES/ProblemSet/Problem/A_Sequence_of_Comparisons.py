testcase=int(input())
for test in range(testcase):
    string=input()
    if "<" in string and ">" in string:
        print("?")
    else:
        if ">" in string:
            print(">")
        elif "<" in string:
            print("<")
        else:
            print("=")