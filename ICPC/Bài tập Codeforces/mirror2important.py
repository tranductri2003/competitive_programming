testcase=int(input())
allowed=['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y']

def check(chuoi):
    chuoimoi = chuoi[::-1]
    if chuoi==chuoimoi:
        return True
    else:
        return False



for i in range(0,testcase):
    chuoi=input()
    test=list()
    start=0
    end=0
    n=len(chuoi)
    for i in range(0,n):
        if chuoi[i] not in allowed:
            end=i
            test.append(chuoi[start:end])
            start=i+1
    if chuoi[n-1] in allowed:
        test.append(chuoi[start:])

    test.sort(key = len,reverse=True)
    for bai in test:
        
