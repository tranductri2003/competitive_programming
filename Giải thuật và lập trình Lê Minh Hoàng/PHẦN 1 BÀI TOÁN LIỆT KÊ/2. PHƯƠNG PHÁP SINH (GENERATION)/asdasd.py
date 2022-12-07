"""
Xét từ cuối về đầu:
Nếu thầy bằng 0 thì thay bằng 1 và trước đó đều bằng 0
Nếu không thấy thì toàn là số 1, in ra là đáp án bài toán
"""
n=int(input())
a=[0]*n
i=n-1
time=0
while i>=0:
    if a[i]==0:
        a[i]=1
        for j in range(n-1,i,-1):
            a[j]=0
        i=n-1     #reset lại từ đầu
    for k in range(0,n):
        print(a[k],end="")
    i-=1
    print(" ")
    time+=1

print(time)   #time=2^n-1


