n=int(input())
a=[0]*n
def backtrack(i):  #Đề quy tạo ra một dãy các vòng lặp for nối tiếp nhau
    for value in range(0,2):
        a[i]=value
        if i==n-1:
            print(*a)
        else:
            backtrack(i+1)

backtrack(0)  #Chạy từ phần tử a[0] đến a[n-1]

"""
a=[0]*3

for v in range(0,2):
    a[0]=v
    for b in range(0,2):
        a[1]=b
        for n in range(0,2):
            a[2]=n
            print(*a)
"""