


testcase=int(input())

for testcase in range(0,testcase):
    chuoi=input()
    chuoimoi=list()
    for i in range(0,len(chuoi)):
        if chuoi[i]=="u" or chuoi[i]=="e" or chuoi[i]=="o" or chuoi[i]=="a" or chuoi[i]=="i" or chuoi[i]=="U" or chuoi[i]=="E" or chuoi[i]=="O" or chuoi[i]=="A" or chuoi[i]=="I" :
            chuoimoi.append(chuoi[i].upper())
        else:
            chuoimoi.append(chuoi[i].lower())
    for i in range(0,len(chuoimoi)):
        print(chuoimoi[i], end="")
    print("")

