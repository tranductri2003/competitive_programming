from collections import defaultdict


def print_rectangle(s, n, m):

    matrix = [[0] * m for _ in range(n)]
    index = 0

    for i in range(n):
        for j in range(m):
            matrix[i][j] = s[index]
            index += 1

    return matrix


def check(s):
    n = len(s)
    for i in range(1, n+1):
        if n % i == 0:
            t = i
            matrix = print_rectangle(s, n//i, i)
            rows = len(matrix)
            cols = len(matrix[0])

            # Kiểm tra hàng
            for i in range(rows):
                for j in range(cols - 1):
                    if matrix[i][j] == matrix[i][j + 1]:
                        print("FALSE1")
                        quit()

            # Kiểm tra cột
            for j in range(cols):
                for i in range(rows - 1):
                    if matrix[i][j] == matrix[i + 1][j]:

                        print("FALSE2", j, i, t, n//t)
                        print(matrix[i][j])
                        print(matrix[i+1][j])
                        quit()


# check("tomato")
check("abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdef")
# matrix = print_rectangle("abcdefgahciejgakliejmaklnejmakonejmakonepmakonepqakonepqakonrpqakonrpqakonrpqakosrpqakosrpqakosrpqakosrpqakosrpqakosrpqatosrpqatosrpqatosrpqatosrpqatosrpqatosrpqatosrpqatosrpqatosrpqatosrpqatosrpqatosrpqatosrpqatosrpqatosrpqatosrpqatosrpqat", 2, 13)
# if matrix:
#     for row in matrix:
#         print(' '.join(row))
# def uoc(n):
#     i = 1
#     data = []
#     while i*i <= n:
#         if i*i == n:
#             data.append(i)
#         else:
#             if n % i == 0:
#                 data.append(i)
#                 data.append(n//i)
#         i += 1

#     return data

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     data = uoc(n)
#     data.sort()
#     data = data[:-1]
#     res = defaultdict(lambda: -1)
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for i in range(1, n+1):
#         if res[i] == -1:
#             time = 0
#             res[i] = alphabet[time]
#             time += 1
#             for num in data:
#                 if res[i+num] != -1:
#                     pass
#                 else:
#                     res[i+num] = alphabet[time % 26]
#                     time += 1

#     for i in range(1, n+1):
#         print(res[i], end="")
#     print()
