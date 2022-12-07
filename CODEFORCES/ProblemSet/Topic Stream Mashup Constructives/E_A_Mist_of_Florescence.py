# Ý tưởng
"""
AAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAA

BBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBB

CCCCCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCC

DDDDDDDDDDDDDDDDDD
DDDDDDDDDDDDDDDDDD
DDDDDDDDDDDDDDDDDD
"""

"""
12 dòng nhân cho 50 ký tự

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
"""
A, B, C, D = list(map(int, input().split()))

matrix = []
for i in range(48):
    matrix.append([])
    for j in range(50):
        if i < 12:
            matrix[i].append("A")
        elif i < 24:
            matrix[i].append("B")
        elif i < 36:
            matrix[i].append("C")
        else:
            matrix[i].append("D")

A -= 1
B -= 1
C -= 1
D -= 1

# A trồng ở B
# B trồng ở A
# C trồng ở D
# D trồng ở C


# Với hoa A thì trồng ở khu vực B:
for i in range(13, 13+12, 2):  # Phải lên 1 hàng để không bị dính
    if A == 0:
        break
    for j in range(0, 50, 2):
        if A == 0:
            break
        matrix[i][j] = "A"
        A -= 1

# Với hoa B thì trồng ở khu vực A:
for i in range(0, 0+12, 2):
    if B == 0:
        break
    for j in range(0, 50, 2):
        if B == 0:
            break
        matrix[i][j] = "B"
        B -= 1


# Với hoa C thì trồng ở khu vực D:
for i in range(37, 37+12, 2):  # Phải lên 1 hàng để không bị dính
    if C == 0:
        break
    for j in range(0, 50, 2):
        if C == 0:
            break
        matrix[i][j] = "C"
        C -= 1

# Với hoa D thì trồng ở khu vực C:
for i in range(24, 24+12, 2):
    if D == 0:
        break
    for j in range(0, 50, 2):
        if D == 0:
            break
        matrix[i][j] = "D"
        D -= 1

print(48, 50)
for i in range(48):
    print(*matrix[i], sep="")


# print("blue")
# for i in range(0, 48):
#     for j in range(50):
#         if matrix[i][j] == "A":
#             print(j, 48-i)
# print("red")
# for i in range(0, 48):
#     for j in range(50):
#         if matrix[i][j] == "B":
#             print(j, 48-i)
# print("green")
# for i in range(0, 48):
#     for j in range(50):
#         if matrix[i][j] == "C":
#             print(j, 48-i)
# print("yellow")
# for i in range(0, 48):
#     for j in range(50):
#         if matrix[i][j] == "D":
#             print(j, 48-i)


# https://pasteboard.co/cczzDDeik5Yr.png
"""
code ve hinh
blue
1 48
3 48
5 48
7 48
9 48
11 48
13 48
15 48
17 48
19 48
21 48
23 48
25 48
27 48
29 48
31 48
33 48
35 48
37 48
39 48
41 48
43 48
45 48
47 48
49 48
0 47
1 47
2 47
3 47
4 47
5 47
6 47
7 47
8 47
9 47
10 47
11 47
12 47
13 47
14 47
15 47
16 47
17 47
18 47
19 47
20 47
21 47
22 47
23 47
24 47
25 47
26 47
27 47
28 47
29 47
30 47
31 47
32 47
33 47
34 47
35 47
36 47
37 47
38 47
39 47
40 47
41 47
42 47
43 47
44 47
45 47
46 47
47 47
48 47
49 47
1 46
3 46
5 46
7 46
9 46
11 46
13 46
15 46
17 46
19 46
21 46
23 46
25 46
27 46
29 46
31 46
33 46
35 46
37 46
39 46
41 46
43 46
45 46
47 46
48 46
49 46
0 45
1 45
2 45
3 45
4 45
5 45
6 45
7 45
8 45
9 45
10 45
11 45
12 45
13 45
14 45
15 45
16 45
17 45
18 45
19 45
20 45
21 45
22 45
23 45
24 45
25 45
26 45
27 45
28 45
29 45
30 45
31 45
32 45
33 45
34 45
35 45
36 45
37 45
38 45
39 45
40 45
41 45
42 45
43 45
44 45
45 45
46 45
47 45
48 45
49 45
0 44
1 44
2 44
3 44
4 44
5 44
6 44
7 44
8 44
9 44
10 44
11 44
12 44
13 44
14 44
15 44
16 44
17 44
18 44
19 44
20 44
21 44
22 44
23 44
24 44
25 44
26 44
27 44
28 44
29 44
30 44
31 44
32 44
33 44
34 44
35 44
36 44
37 44
38 44
39 44
40 44
41 44
42 44
43 44
44 44
45 44
46 44
47 44
48 44
49 44
0 43
1 43
2 43
3 43
4 43
5 43
6 43
7 43
8 43
9 43
10 43
11 43
12 43
13 43
14 43
15 43
16 43
17 43
18 43
19 43
20 43
21 43
22 43
23 43
24 43
25 43
26 43
27 43
28 43
29 43
30 43
31 43
32 43
33 43
34 43
35 43
36 43
37 43
38 43
39 43
40 43
41 43
42 43
43 43
44 43
45 43
46 43
47 43
48 43
49 43
0 42
1 42
2 42
3 42
4 42
5 42
6 42
7 42
8 42
9 42
10 42
11 42
12 42
13 42
14 42
15 42
16 42
17 42
18 42
19 42
20 42
21 42
22 42
23 42
24 42
25 42
26 42
27 42
28 42
29 42
30 42
31 42
32 42
33 42
34 42
35 42
36 42
37 42
38 42
39 42
40 42
41 42
42 42
43 42
44 42
45 42
46 42
47 42
48 42
49 42
0 41
1 41
2 41
3 41
4 41
5 41
6 41
7 41
8 41
9 41
10 41
11 41
12 41
13 41
14 41
15 41
16 41
17 41
18 41
19 41
20 41
21 41
22 41
23 41
24 41
25 41
26 41
27 41
28 41
29 41
30 41
31 41
32 41
33 41
34 41
35 41
36 41
37 41
38 41
39 41
40 41
41 41
42 41
43 41
44 41
45 41
46 41
47 41
48 41
49 41
0 40
1 40
2 40
3 40
4 40
5 40
6 40
7 40
8 40
9 40
10 40
11 40
12 40
13 40
14 40
15 40
16 40
17 40
18 40
19 40
20 40
21 40
22 40
23 40
24 40
25 40
26 40
27 40
28 40
29 40
30 40
31 40
32 40
33 40
34 40
35 40
36 40
37 40
38 40
39 40
40 40
41 40
42 40
43 40
44 40
45 40
46 40
47 40
48 40
49 40
0 39
1 39
2 39
3 39
4 39
5 39
6 39
7 39
8 39
9 39
10 39
11 39
12 39
13 39
14 39
15 39
16 39
17 39
18 39
19 39
20 39
21 39
22 39
23 39
24 39
25 39
26 39
27 39
28 39
29 39
30 39
31 39
32 39
33 39
34 39
35 39
36 39
37 39
38 39
39 39
40 39
41 39
42 39
43 39
44 39
45 39
46 39
47 39
48 39
49 39
0 38
1 38
2 38
3 38
4 38
5 38
6 38
7 38
8 38
9 38
10 38
11 38
12 38
13 38
14 38
15 38
16 38
17 38
18 38
19 38
20 38
21 38
22 38
23 38
24 38
25 38
26 38
27 38
28 38
29 38
30 38
31 38
32 38
33 38
34 38
35 38
36 38
37 38
38 38
39 38
40 38
41 38
42 38
43 38
44 38
45 38
46 38
47 38
48 38
49 38
0 37
1 37
2 37
3 37
4 37
5 37
6 37
7 37
8 37
9 37
10 37
11 37
12 37
13 37
14 37
15 37
16 37
17 37
18 37
19 37
20 37
21 37
22 37
23 37
24 37
25 37
26 37
27 37
28 37
29 37
30 37
31 37
32 37
33 37
34 37
35 37
36 37
37 37
38 37
39 37
40 37
41 37
42 37
43 37
44 37
45 37
46 37
47 37
48 37
49 37
0 35
2 35
4 35
6 35
8 35
10 35
12 35
14 35
16 35
18 35
20 35
22 35
24 35
26 35
28 35
30 35
32 35
34 35
36 35
38 35
40 35
42 35
44 35
46 35
48 35
0 33
2 33
4 33
6 33
8 33
10 33
12 33
14 33
16 33
18 33
20 33
22 33
24 33
26 33
28 33
30 33
32 33
34 33
36 33
38 33
40 33
42 33
44 33
46 33
red
0 48
2 48
4 48
6 48
8 48
10 48
12 48
14 48
16 48
18 48
20 48
22 48
24 48
26 48
28 48
30 48
32 48
34 48
36 48
38 48
40 48
42 48
44 48
46 48
48 48
0 46
2 46
4 46
6 46
8 46
10 46
12 46
14 46
16 46
18 46
20 46
22 46
24 46
26 46
28 46
30 46
32 46
34 46
36 46
38 46
40 46
42 46
44 46
46 46
0 36
1 36
2 36
3 36
4 36
5 36
6 36
7 36
8 36
9 36
10 36
11 36
12 36
13 36
14 36
15 36
16 36
17 36
18 36
19 36
20 36
21 36
22 36
23 36
24 36
25 36
26 36
27 36
28 36
29 36
30 36
31 36
32 36
33 36
34 36
35 36
36 36
37 36
38 36
39 36
40 36
41 36
42 36
43 36
44 36
45 36
46 36
47 36
48 36
49 36
1 35
3 35
5 35
7 35
9 35
11 35
13 35
15 35
17 35
19 35
21 35
23 35
25 35
27 35
29 35
31 35
33 35
35 35
37 35
39 35
41 35
43 35
45 35
47 35
49 35
0 34
1 34
2 34
3 34
4 34
5 34
6 34
7 34
8 34
9 34
10 34
11 34
12 34
13 34
14 34
15 34
16 34
17 34
18 34
19 34
20 34
21 34
22 34
23 34
24 34
25 34
26 34
27 34
28 34
29 34
30 34
31 34
32 34
33 34
34 34
35 34
36 34
37 34
38 34
39 34
40 34
41 34
42 34
43 34
44 34
45 34
46 34
47 34
48 34
49 34
1 33
3 33
5 33
7 33
9 33
11 33
13 33
15 33
17 33
19 33
21 33
23 33
25 33
27 33
29 33
31 33
33 33
35 33
37 33
39 33
41 33
43 33
45 33
47 33
48 33
49 33
0 32
1 32
2 32
3 32
4 32
5 32
6 32
7 32
8 32
9 32
10 32
11 32
12 32
13 32
14 32
15 32
16 32
17 32
18 32
19 32
20 32
21 32
22 32
23 32
24 32
25 32
26 32
27 32
28 32
29 32
30 32
31 32
32 32
33 32
34 32
35 32
36 32
37 32
38 32
39 32
40 32
41 32
42 32
43 32
44 32
45 32
46 32
47 32
48 32
49 32
0 31
1 31
2 31
3 31
4 31
5 31
6 31
7 31
8 31
9 31
10 31
11 31
12 31
13 31
14 31
15 31
16 31
17 31
18 31
19 31
20 31
21 31
22 31
23 31
24 31
25 31
26 31
27 31
28 31
29 31
30 31
31 31
32 31
33 31
34 31
35 31
36 31
37 31
38 31
39 31
40 31
41 31
42 31
43 31
44 31
45 31
46 31
47 31
48 31
49 31
0 30
1 30
2 30
3 30
4 30
5 30
6 30
7 30
8 30
9 30
10 30
11 30
12 30
13 30
14 30
15 30
16 30
17 30
18 30
19 30
20 30
21 30
22 30
23 30
24 30
25 30
26 30
27 30
28 30
29 30
30 30
31 30
32 30
33 30
34 30
35 30
36 30
37 30
38 30
39 30
40 30
41 30
42 30
43 30
44 30
45 30
46 30
47 30
48 30
49 30
0 29
1 29
2 29
3 29
4 29
5 29
6 29
7 29
8 29
9 29
10 29
11 29
12 29
13 29
14 29
15 29
16 29
17 29
18 29
19 29
20 29
21 29
22 29
23 29
24 29
25 29
26 29
27 29
28 29
29 29
30 29
31 29
32 29
33 29
34 29
35 29
36 29
37 29
38 29
39 29
40 29
41 29
42 29
43 29
44 29
45 29
46 29
47 29
48 29
49 29
0 28
1 28
2 28
3 28
4 28
5 28
6 28
7 28
8 28
9 28
10 28
11 28
12 28
13 28
14 28
15 28
16 28
17 28
18 28
19 28
20 28
21 28
22 28
23 28
24 28
25 28
26 28
27 28
28 28
29 28
30 28
31 28
32 28
33 28
34 28
35 28
36 28
37 28
38 28
39 28
40 28
41 28
42 28
43 28
44 28
45 28
46 28
47 28
48 28
49 28
0 27
1 27
2 27
3 27
4 27
5 27
6 27
7 27
8 27
9 27
10 27
11 27
12 27
13 27
14 27
15 27
16 27
17 27
18 27
19 27
20 27
21 27
22 27
23 27
24 27
25 27
26 27
27 27
28 27
29 27
30 27
31 27
32 27
33 27
34 27
35 27
36 27
37 27
38 27
39 27
40 27
41 27
42 27
43 27
44 27
45 27
46 27
47 27
48 27
49 27
0 26
1 26
2 26
3 26
4 26
5 26
6 26
7 26
8 26
9 26
10 26
11 26
12 26
13 26
14 26
15 26
16 26
17 26
18 26
19 26
20 26
21 26
22 26
23 26
24 26
25 26
26 26
27 26
28 26
29 26
30 26
31 26
32 26
33 26
34 26
35 26
36 26
37 26
38 26
39 26
40 26
41 26
42 26
43 26
44 26
45 26
46 26
47 26
48 26
49 26
0 25
1 25
2 25
3 25
4 25
5 25
6 25
7 25
8 25
9 25
10 25
11 25
12 25
13 25
14 25
15 25
16 25
17 25
18 25
19 25
20 25
21 25
22 25
23 25
24 25
25 25
26 25
27 25
28 25
29 25
30 25
31 25
32 25
33 25
34 25
35 25
36 25
37 25
38 25
39 25
40 25
41 25
42 25
43 25
44 25
45 25
46 25
47 25
48 25
49 25
green
1 24
3 24
5 24
7 24
9 24
11 24
13 24
15 24
17 24
19 24
21 24
23 24
25 24
27 24
29 24
31 24
33 24
35 24
37 24
39 24
41 24
43 24
45 24
47 24
49 24
0 23
1 23
2 23
3 23
4 23
5 23
6 23
7 23
8 23
9 23
10 23
11 23
12 23
13 23
14 23
15 23
16 23
17 23
18 23
19 23
20 23
21 23
22 23
23 23
24 23
25 23
26 23
27 23
28 23
29 23
30 23
31 23
32 23
33 23
34 23
35 23
36 23
37 23
38 23
39 23
40 23
41 23
42 23
43 23
44 23
45 23
46 23
47 23
48 23
49 23
1 22
3 22
5 22
7 22
9 22
11 22
13 22
15 22
17 22
19 22
21 22
23 22
25 22
27 22
29 22
31 22
33 22
35 22
37 22
39 22
41 22
43 22
45 22
47 22
48 22
49 22
0 21
1 21
2 21
3 21
4 21
5 21
6 21
7 21
8 21
9 21
10 21
11 21
12 21
13 21
14 21
15 21
16 21
17 21
18 21
19 21
20 21
21 21
22 21
23 21
24 21
25 21
26 21
27 21
28 21
29 21
30 21
31 21
32 21
33 21
34 21
35 21
36 21
37 21
38 21
39 21
40 21
41 21
42 21
43 21
44 21
45 21
46 21
47 21
48 21
49 21
0 20
1 20
2 20
3 20
4 20
5 20
6 20
7 20
8 20
9 20
10 20
11 20
12 20
13 20
14 20
15 20
16 20
17 20
18 20
19 20
20 20
21 20
22 20
23 20
24 20
25 20
26 20
27 20
28 20
29 20
30 20
31 20
32 20
33 20
34 20
35 20
36 20
37 20
38 20
39 20
40 20
41 20
42 20
43 20
44 20
45 20
46 20
47 20
48 20
49 20
0 19
1 19
2 19
3 19
4 19
5 19
6 19
7 19
8 19
9 19
10 19
11 19
12 19
13 19
14 19
15 19
16 19
17 19
18 19
19 19
20 19
21 19
22 19
23 19
24 19
25 19
26 19
27 19
28 19
29 19
30 19
31 19
32 19
33 19
34 19
35 19
36 19
37 19
38 19
39 19
40 19
41 19
42 19
43 19
44 19
45 19
46 19
47 19
48 19
49 19
0 18
1 18
2 18
3 18
4 18
5 18
6 18
7 18
8 18
9 18
10 18
11 18
12 18
13 18
14 18
15 18
16 18
17 18
18 18
19 18
20 18
21 18
22 18
23 18
24 18
25 18
26 18
27 18
28 18
29 18
30 18
31 18
32 18
33 18
34 18
35 18
36 18
37 18
38 18
39 18
40 18
41 18
42 18
43 18
44 18
45 18
46 18
47 18
48 18
49 18
0 17
1 17
2 17
3 17
4 17
5 17
6 17
7 17
8 17
9 17
10 17
11 17
12 17
13 17
14 17
15 17
16 17
17 17
18 17
19 17
20 17
21 17
22 17
23 17
24 17
25 17
26 17
27 17
28 17
29 17
30 17
31 17
32 17
33 17
34 17
35 17
36 17
37 17
38 17
39 17
40 17
41 17
42 17
43 17
44 17
45 17
46 17
47 17
48 17
49 17
0 16
1 16
2 16
3 16
4 16
5 16
6 16
7 16
8 16
9 16
10 16
11 16
12 16
13 16
14 16
15 16
16 16
17 16
18 16
19 16
20 16
21 16
22 16
23 16
24 16
25 16
26 16
27 16
28 16
29 16
30 16
31 16
32 16
33 16
34 16
35 16
36 16
37 16
38 16
39 16
40 16
41 16
42 16
43 16
44 16
45 16
46 16
47 16
48 16
49 16
0 15
1 15
2 15
3 15
4 15
5 15
6 15
7 15
8 15
9 15
10 15
11 15
12 15
13 15
14 15
15 15
16 15
17 15
18 15
19 15
20 15
21 15
22 15
23 15
24 15
25 15
26 15
27 15
28 15
29 15
30 15
31 15
32 15
33 15
34 15
35 15
36 15
37 15
38 15
39 15
40 15
41 15
42 15
43 15
44 15
45 15
46 15
47 15
48 15
49 15
0 14
1 14
2 14
3 14
4 14
5 14
6 14
7 14
8 14
9 14
10 14
11 14
12 14
13 14
14 14
15 14
16 14
17 14
18 14
19 14
20 14
21 14
22 14
23 14
24 14
25 14
26 14
27 14
28 14
29 14
30 14
31 14
32 14
33 14
34 14
35 14
36 14
37 14
38 14
39 14
40 14
41 14
42 14
43 14
44 14
45 14
46 14
47 14
48 14
49 14
0 13
1 13
2 13
3 13
4 13
5 13
6 13
7 13
8 13
9 13
10 13
11 13
12 13
13 13
14 13
15 13
16 13
17 13
18 13
19 13
20 13
21 13
22 13
23 13
24 13
25 13
26 13
27 13
28 13
29 13
30 13
31 13
32 13
33 13
34 13
35 13
36 13
37 13
38 13
39 13
40 13
41 13
42 13
43 13
44 13
45 13
46 13
47 13
48 13
49 13
0 11
2 11
4 11
6 11
8 11
10 11
12 11
14 11
16 11
18 11
20 11
22 11
24 11
26 11
28 11
30 11
32 11
34 11
36 11
38 11
40 11
42 11
44 11
46 11
48 11
0 9
2 9
4 9
6 9
8 9
10 9
12 9
14 9
16 9
18 9
20 9
22 9
24 9
26 9
28 9
30 9
32 9
34 9
36 9
38 9
40 9
42 9
44 9
46 9
yellow
0 24
2 24
4 24
6 24
8 24
10 24
12 24
14 24
16 24
18 24
20 24
22 24
24 24
26 24
28 24
30 24
32 24
34 24
36 24
38 24
40 24
42 24
44 24
46 24
48 24
0 22
2 22
4 22
6 22
8 22
10 22
12 22
14 22
16 22
18 22
20 22
22 22
24 22
26 22
28 22
30 22
32 22
34 22
36 22
38 22
40 22
42 22
44 22
46 22
0 12
1 12
2 12
3 12
4 12
5 12
6 12
7 12
8 12
9 12
10 12
11 12
12 12
13 12
14 12
15 12
16 12
17 12
18 12
19 12
20 12
21 12
22 12
23 12
24 12
25 12
26 12
27 12
28 12
29 12
30 12
31 12
32 12
33 12
34 12
35 12
36 12
37 12
38 12
39 12
40 12
41 12
42 12
43 12
44 12
45 12
46 12
47 12
48 12
49 12
1 11
3 11
5 11
7 11
9 11
11 11
13 11
15 11
17 11
19 11
21 11
23 11
25 11
27 11
29 11
31 11
33 11
35 11
37 11
39 11
41 11
43 11
45 11
47 11
49 11
0 10
1 10
2 10
3 10
4 10
5 10
6 10
7 10
8 10
9 10
10 10
11 10
12 10
13 10
14 10
15 10
16 10
17 10
18 10
19 10
20 10
21 10
22 10
23 10
24 10
25 10
26 10
27 10
28 10
29 10
30 10
31 10
32 10
33 10
34 10
35 10
36 10
37 10
38 10
39 10
40 10
41 10
42 10
43 10
44 10
45 10
46 10
47 10
48 10
49 10
1 9
3 9
5 9
7 9
9 9
11 9
13 9
15 9
17 9
19 9
21 9
23 9
25 9
27 9
29 9
31 9
33 9
35 9
37 9
39 9
41 9
43 9
45 9
47 9
48 9
49 9
0 8
1 8
2 8
3 8
4 8
5 8
6 8
7 8
8 8
9 8
10 8
11 8
12 8
13 8
14 8
15 8
16 8
17 8
18 8
19 8
20 8
21 8
22 8
23 8
24 8
25 8
26 8
27 8
28 8
29 8
30 8
31 8
32 8
33 8
34 8
35 8
36 8
37 8
38 8
39 8
40 8
41 8
42 8
43 8
44 8
45 8
46 8
47 8
48 8
49 8
0 7
1 7
2 7
3 7
4 7
5 7
6 7
7 7
8 7
9 7
10 7
11 7
12 7
13 7
14 7
15 7
16 7
17 7
18 7
19 7
20 7
21 7
22 7
23 7
24 7
25 7
26 7
27 7
28 7
29 7
30 7
31 7
32 7
33 7
34 7
35 7
36 7
37 7
38 7
39 7
40 7
41 7
42 7
43 7
44 7
45 7
46 7
47 7
48 7
49 7
0 6
1 6
2 6
3 6
4 6
5 6
6 6
7 6
8 6
9 6
10 6
11 6
12 6
13 6
14 6
15 6
16 6
17 6
18 6
19 6
20 6
21 6
22 6
23 6
24 6
25 6
26 6
27 6
28 6
29 6
30 6
31 6
32 6
33 6
34 6
35 6
36 6
37 6
38 6
39 6
40 6
41 6
42 6
43 6
44 6
45 6
46 6
47 6
48 6
49 6
0 5
1 5
2 5
3 5
4 5
5 5
6 5
7 5
8 5
9 5
10 5
11 5
12 5
13 5
14 5
15 5
16 5
17 5
18 5
19 5
20 5
21 5
22 5
23 5
24 5
25 5
26 5
27 5
28 5
29 5
30 5
31 5
32 5
33 5
34 5
35 5
36 5
37 5
38 5
39 5
40 5
41 5
42 5
43 5
44 5
45 5
46 5
47 5
48 5
49 5
0 4
1 4
2 4
3 4
4 4
5 4
6 4
7 4
8 4
9 4
10 4
11 4
12 4
13 4
14 4
15 4
16 4
17 4
18 4
19 4
20 4
21 4
22 4
23 4
24 4
25 4
26 4
27 4
28 4
29 4
30 4
31 4
32 4
33 4
34 4
35 4
36 4
37 4
38 4
39 4
40 4
41 4
42 4
43 4
44 4
45 4
46 4
47 4
48 4
49 4
0 3
1 3
2 3
3 3
4 3
5 3
6 3
7 3
8 3
9 3
10 3
11 3
12 3
13 3
14 3
15 3
16 3
17 3
18 3
19 3
20 3
21 3
22 3
23 3
24 3
25 3
26 3
27 3
28 3
29 3
30 3
31 3
32 3
33 3
34 3
35 3
36 3
37 3
38 3
39 3
40 3
41 3
42 3
43 3
44 3
45 3
46 3
47 3
48 3
49 3
0 2
1 2
2 2
3 2
4 2
5 2
6 2
7 2
8 2
9 2
10 2
11 2
12 2
13 2
14 2
15 2
16 2
17 2
18 2
19 2
20 2
21 2
22 2
23 2
24 2
25 2
26 2
27 2
28 2
29 2
30 2
31 2
32 2
33 2
34 2
35 2
36 2
37 2
38 2
39 2
40 2
41 2
42 2
43 2
44 2
45 2
46 2
47 2
48 2
49 2
0 1
1 1
2 1
3 1
4 1
5 1
6 1
7 1
8 1
9 1
10 1
11 1
12 1
13 1
14 1
15 1
16 1
17 1
18 1
19 1
20 1
21 1
22 1
23 1
24 1
25 1
26 1
27 1
28 1
29 1
30 1
31 1
32 1
33 1
34 1
35 1
36 1
37 1
38 1
39 1
40 1
41 1
42 1
43 1
44 1
45 1
46 1
47 1
48 1
49 1
"""
