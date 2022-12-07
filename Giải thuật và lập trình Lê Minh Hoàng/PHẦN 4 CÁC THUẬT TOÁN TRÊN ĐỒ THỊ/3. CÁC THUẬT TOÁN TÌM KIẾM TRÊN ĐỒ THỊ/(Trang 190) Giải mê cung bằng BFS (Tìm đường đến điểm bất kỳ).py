
#m: Chiều dài, n: Chiều rộng


def coordinates(number,m,n):    #Coordinate: tọa độ, number: vị trí cần tìm tọa độ xy, m: chiều ngang, n: chiều dọc
    y=0
    x=0
    while number>m:
        number-=m
        y+=1
    x=number-1
    return x,y


print("Mời bạn nhập kích thước chiều ngang m, chiều dọc n: ",end=" ")
m,n=list(map(int,input().split()))

matrix=[]

blockedlist=[]


for i in range(0,n):
    matrix.append([])
    for j in range(0,m):
        #matrix[i].append(i*m+j+1)
        matrix[i].append(0)

print("Mời bạn nhập số ô có cạm bẫy: ",end="")
obstacle=int(input())
print("Mời bạn nhập tọa độ các ô có cạm bẫy: ",end="")
for i in range(0,obstacle):
    X=int(input())
    x,y=coordinates(X,m,n)
    matrix[y][x]="X"   #Máy tính xét ma trận theo chiều dọc i trước rồi mới qua chiều ngang j
    blockedlist.append(X)

print("Mời bạn nhập ô nhà thám hiểm đang đứng: ",end="")
E=int(input())
x,y=coordinates(E,m,n)
matrix[y][x]="E"

print("Mời bạn nhập ô nhà thám hiểm muốn đến: ",end="")
F=int(input())
x,y=coordinates(F,m,n)
matrix[y][x]="Đ"

#Khởi tạo hàng đợi ban đầu chỉ gồm một ô E
queue=[]
queue.append(E)

#Khởi tạo truy vết
trace=[0]*(m*n+1)
trace[E]=-1

#Tìm tất cả các đường có thể đi
while len(queue)!=0:   #BFS đến khi không còn phần tử nào trong queue
    u=queue[0]          
    queue.pop(0)
    adjacencyList=[]  #Danh sách các ô kề với ô đang xét
    x,y=coordinates(u,m,n)
    if x-1>=0:
        adjacencyList.append(u-1)
    if x+1<=m-1:
        adjacencyList.append(u+1)
    if y-1>=0:
        adjacencyList.append(u-m)
    if y+1<=n-1:
        adjacencyList.append(u+m)

    for v in adjacencyList:
        if trace[v]==0 and v not in blockedlist:
            trace[v]=u
            queue.append(v)       #Thêm vào queue

print(f"Từ nơi nhà thám hiểm đang đứng (ô {E}), ông ấy có thể đi đến các ô: ",end="")
for v in range(1,m*n+1):
    if trace[v]!=0:
        print(v,end=", ")



print(f"Con đường từ dẫn từ nơi nhà thám hiểm đang đứng (ô {E}) đến ô {F} là: ",end="")
while F!=E:
    print(F,end=" <- ")
    F=trace[F]
print(E)

print("Bản đồ tổng quát là: ")
for i in range(0,n):
    print(*matrix[i])

for i in range(0,n):
    for j in range(0,m):
        if matrix[i][j]==0:
            matrix[i][j]=i*m+j+1

print("Bạn có thể tham khảo đường đi là: ")
for i in range(0,n):
    print(*matrix[i])
"""
m,n=7,4
số ô cấm: 13
tọa độ cấm:
4
5
7
8
10
13
15
19
21
23
24
25
27
tọa độ nhà thám hiểm: 18
"""

#################################################################
#                             _`				#
#                          _ooOoo_				#
#                         o8888888o				#
#                         88" . "88				#
#                         (| -_- |)				#
#                         O\  =  /O				#
#                      ____/`---'\____				#
#                    .'  \\|     |//  `.			#
#                   /  \\|||  :  |||//  \			#
#                  /  _||||| -:- |||||_  \			#
#                  |   | \\\  -  /'| |   |			#
#                  | \_|  `\`---'//  |_/ |			#
#                  \  .-\__ `-. -'__/-.  /			#
#                ___`. .'  /--.--\  `. .'___			#
#             ."" '<  `.___\_<|>_/___.' _> \"".			#
#            | | :  `- \`. ;`. _/; .'/ /  .' ; |		#
#            \  \ `-.   \_\_`. _.'_/_/  -' _.' /		#
#=============`-.`___`-.__\ \___  /__.-'_.'_.-'=================#
#                           `=--=-'                    



#          _.-/`)
#         // / / )
#      .=// / / / )
#     //`/ / / / /
#    // /     ` /
#   ||         /
#    \\       /
#     ))    .'
#    //    /
#         /
"""
15 15
129
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 30 31 33 34 35 36 37 38 39 40 41 42 43 45 46 50 52 54 58 60 61 62 63 65 67 69 71 73 74 75 76 78 82 86 90 91 93 94 95 97 98 99 100 101 102 103 105 106 110 112 118 120 121 123 124 125 127 128 129 131 132 133 135 136 146 150 151 153 154 155 156 157 158 159 160 161 163 164 165 166 168 176 180 181 183 185 186 187 188 189 191 192 193 195 196 198 204 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225   
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
30
31
33
34
35
36
37
38
39
40
41
42
43
45
46
50
52
54
58
60
61
62
63
65
67
69
71
73
74
75
76
78
82
86
90
91
93
94
95
97
98
99
100
101
102
103
105
106
110
112
118
120
121
123
124
125
127
128
129
131
132
133
135
136
146
150
151
153
154
155
156
157
158
159
160
161
163
164
165
166
168
176
180
181
183
185
186
187
188
189
191
192
193
195
196
198
204
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
"""