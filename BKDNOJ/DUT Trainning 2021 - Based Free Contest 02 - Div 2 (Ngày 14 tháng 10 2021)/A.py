#n: số đường thẳng song song với trục oy
#m: số đường thẳng song song với trục ox
n,m=list(map(int,input().split()))
#Dòng thứ hai gồm n số nguyên x1, x2, . . . , xn (−109 ≤ xi ≤ 109, xi < xi+1) - mô tả các đường thẳng song song với trục Oy theo thứ tự từ trái qua phải.
x= list(map(int,input().split()))
#Dòng thứ ba gồm m số nguyên y1, y2, . . . , ym (−109 ≤ yi ≤ 109, yi < yi+1) - mô tả các đường thẳng song song với trục Ox theo thứ tự từ dưới lên trên.
y=list(map(int,input().split()))

for chieurong in range(1,n): #Song song với Oy
    for chieudai in range(1,m): #Song song với Ox
        