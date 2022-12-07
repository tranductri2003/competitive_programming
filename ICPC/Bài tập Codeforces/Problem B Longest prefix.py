def check(string1,string2):
    demphanphoi=[0]*26



    for tu in string2:
        demphanphoi[ord(tu)-97]+=1
    length=0
    
    for tu in string1:
        if demphanphoi[ord(tu)-97]>0:
            length+=1
            demphanphoi[ord(tu)-97]-=1  #Trừ để tính tiếp trường hợp gặp lại
        else:
            break
    print(length)







testcase=int(input())
for i in range(0,testcase):
    a,b=map(str,input().split())
    check(a,b)