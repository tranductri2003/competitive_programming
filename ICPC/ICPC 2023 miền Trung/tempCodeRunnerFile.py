data = []
while True:
    s = input()
    if s == "":
        break
    else:
        data.append(s)

newData = []
for tu in data:
    newTu = tu.split(" ")
    for t in newTu:
        newData.append(t)
        



if "Welcome" in newData and "Hue" in newData and "University" in newData and "of" in newData and "Sciences" in newData:
    print("Yes")
else:
    print("No")
