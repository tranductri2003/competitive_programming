from unittest import TestCase


testcase=int(input())
for test in range(testcase):
    string=input()
    string=list(string)
    for i in range(0,len(string)):
        string[i]=ord(string[i])-96
    if len(string)!=len(set(string)) or max(string)!=len(string):
        print("NO")
    else:
        i=0
        j=len(string)-1
        for k in range(max(string),0,-1):
            if string[i]!=k and string[j]!=k:
                print("NO")
                break
            else:
                if string[i]==string[j]==k:
                    print("YES")
                    break
                if string[i]==k:
                    i+=1
                elif string[j]==k:
                    j-=1

            