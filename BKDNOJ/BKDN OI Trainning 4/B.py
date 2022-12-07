data = []

while True:
    s = input()
    if s == "=":
        data = "".join(data)
        # print(int(eval(data)))
        print(int(eval(data)))
        break
    if s == "/":
        data.append("//")
    else:
        data.append(s)
