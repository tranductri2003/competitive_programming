t=int(input())
for _ in range(t):
    string=input()
    keys=[]
    stop=True
    for i in range(0,len(string)):
        if string[i]=="r" or string[i]=="g" or string[i]=="b":
            keys.append(string[i])
        else:
            if string[i]=="R":
                if 'r' in keys:
                    pass
                else:
                    print("NO")
                    stop=False
                    break
            elif string[i]=="G":
                if 'g' in keys:
                    pass
                else:
                    print("NO")
                    stop=False
                    break
            else:
                if 'b' in keys:
                    pass
                    break
                else:
                    print("NO")
                    stop=False
                    break
    if stop==True:
        print("YES")
            