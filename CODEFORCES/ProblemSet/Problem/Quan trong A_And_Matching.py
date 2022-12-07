"""
Let's define c(x), the compliment of x, as the number x after changing all bits 0 to 1 and vice versa, for example c(1100102)=0011012.

It can be shown that c(x)=x⊕(n−1). Remember that n−1=11...112 since n is a power of 2.

We will separate the problem into three cases.

Case k=0:

In this case it is possible to pair x with c(x) for 0≤x<n2, getting ∑x=0n2−1x&c(x)=0.

Case 0<k<n-1:

In this case it is possible to pair each element with its compliment except 0, k, c(k) and n−1, and then pair 0 with c(k) and k with n−1, 0&c(k)=0 and k&(n−1)=k.

Case k=n−1:

There are many constructions that work in this case, if n=4 there is no solution, if n≥8 it is possible to construct the answer in the following way:

It is possible to pair n−1 with n−2, n−3 with 1, 0 with 2 and all other elements with their compliments.

(n−1)&(n−2)=n−2, for example 11112&11102=11102
(n−3)&1=1, for example 11012&00012=00012
0&2=0, for example 00002&00102=00002
All other elements can be paired with their complements and x&c(x)=0
Note that (n−2)+1+0+0+...+0=n−1.

Each case can be implemented in O(n).
"""
# import math
# n=8
# maxlen=int(math.log(n,2))


# def inverse(str,n):
#     res=''
#     for i in range(0,n):
#         if str[i]=="1":
#             res+='0'
#         else:
#             res+='1'
#     return res
# for i in range(0,8):
#     current=bin(i)[2:]
#     current="0"*(maxlen-len(current))+current
#     print(current,inverse(current,maxlen))
#     print(int(current,2), int(inverse(current,maxlen),2))



#!    0 thì với mọi số đều bằng 0
#!    n-1 với k thì luôn bằng k

#! Suy ra bình thường, nếu k=0 thì nối mỗi số với đảo bit của nó
#!Nếu k<n-1 thì ta nối mỗi số với đảo bit của nó, còn k nối với n-1, đảo bit của k nối với 0
#!Nếu k==n-1:
#          Nếu n<=4: In ra -1
#          Ngược lại, ta bắt cặp n-2 và n-1 được n-2
#Tiếp theo, bắt cặp 1 và n-3 để được 1, tổng là n-1= k
#Tiếp theo, bắt cặp 0 và 2 được 0
#Các cặp còn lại bắt bình thường



t=int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    if k==0:
        for i in range(0,n//2):
            print(i,n-1-i)
    elif 0<k<n-1:
# In this case it is possible to pair each element with
# its compliment except 0, k, c(k) and n−1, and 
# then pair 0 with c(k) and k with n−1, 0&c(k)=0 and k&(n−1)=k. 
        print(k,n-1)
        print(n-1-k,0)
        for i in range(0,n//2):
            if i in (0,k,n-1,n-1-k):
                pass
            else:
                print(i,n-1-i)
    elif k==n-1:
        if n<=4: 
            print(-1)
        else:
            print(k-1,n-1) #Tạo ra k-1
            print(1,n-3)
            print(2,0)
            for i in range(0,n//2):
                if i in (0,1,2,n-3,n-2,n-1):
                    pass
                else:
                    print(i,n-1-i)
                
