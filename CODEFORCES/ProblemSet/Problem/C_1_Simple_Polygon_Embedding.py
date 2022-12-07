
#?		 /\_/\
#?		(= ._.)
#?		/ >WA \>AC
#//     WELCOME TO MY CODING SPACE
#!      Filename: C_1_Simple_Polygon_Embedding.py
#*      Folder: D:\Code\Python\Codeforces\ProblemSet
#?      Author: TranDucTri2003
#TODO   CreatedAt: 2022-05-06 22:29:43

import math

#In ra cạnh của hình vuông nhỏ nhất có thể ôm trọn được hình đa giác đều 2 n cạnh
t=int(input())
for _ in range(t):
    n=int(input())
    S=(2*n)/(4*math.tan(math.pi/(2*n)))
    d=2*S/(2*n)*2
    print(d)