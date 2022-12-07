testcase=int(input())

for bai in range(0,testcase):
    mangdemphanphoi=[0]*100000
    sokenh=int(input())
    for kenh in range(0,sokenh):
        kenh=input()
        mangdemphanphoi[(int(kenh[kenh.index(" ")+1:]))]+=1
    print(mangdemphanphoi.index(max(mangdemphanphoi)))
    