N=input()

sochuso=len(N)
chusocuoicung=N[sochuso-1]

def kiemtra(n):
    if n == 1:
        return False
        quit()
    for i in range(2,n):
        if int(n)%i==0:
            break
    else:
        return True


if kiemtra(int(chusocuoicung))!=True:
    print("NO")
if kiemtra(int(chusocuoicung))==True:
    if kiemtra(int(N))==True and kiemtra(int(chusocuoicung))==True:
        print("YES")
    else:
        print("NO")