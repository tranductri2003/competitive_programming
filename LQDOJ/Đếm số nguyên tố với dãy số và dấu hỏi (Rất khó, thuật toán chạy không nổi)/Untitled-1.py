


listchiadu=list()

def kiemtra(list):
    for num in list:
        if num!=0:
            break
    else:
        return True

listchiadu=[0,0,0,1]
if kiemtra(listchiadu)!=True:
    print("No")
if kiemtra(listchiadu)==True:
    print("Yes")