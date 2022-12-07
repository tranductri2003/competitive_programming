n=int(input())

def collatz(i):
    if i==1:
        print(i,end=" ") #Phần neo
    else:
        if i%2==0:
            collatz(i//2)
            print("x 2",end=" ")
        else:
            collatz(3*i+1)
            print(" // 3 ",end=" ")
print(n,end=" = ")
collatz(n)
"""
Theo giả thuyết Collatz, ví dụ n=10
Muốn tìm số 10 thì ta tìm số 5, tìm được số 5 rồi ta viết x 2 phía sau nó
Muốn tìm số 5 thì ta tìm số 16, tìm được số 16 rồi ta //3 phía sau nó
Muốn tìm số 16 thì ta tìm số 8, tìm được số 8 rồi ta viết x2 phía sau nó
Muốn tìm số 8 thì ta tìm số 4, tìm được số 4 rồi thì ta viết  x2 phía sau nó
Muốn tìm số 4 thì ta tìm số 2, tìm được số 2 rồi thì ta viết x2 phía sau nó
Muốn tìm số 2 thì ta tìm số 1, tìm được số 1 rồi thì ta viết x2 phía sau nó
Muốn tìm số 1 thì ta tìm số 1, đối với số 1 ta in luôn số 1.

Vậy nên, ta in số 1, x2, x2,x2,x2,//3,x2
"""