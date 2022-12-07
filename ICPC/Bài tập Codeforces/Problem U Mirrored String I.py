testcase=int(input())
allowed=['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y']
for i in range(0,testcase):
    chuoi=input()
    for i in chuoi:
        if i not in allowed:
            print("no")
            break
    else:
        chuoimoi = chuoi[::-1]
        if chuoi==chuoimoi:
            print("yes")
        else:
            print("no")