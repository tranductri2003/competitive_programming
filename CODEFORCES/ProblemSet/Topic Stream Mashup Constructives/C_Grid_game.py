
# ? -----------------------------------------------------------------------------------------------------
# ?　　　　　　　　　　　 ∧＿∧
# ?　　　　　 ∧＿∧ 　 （´<_｀ ）
# ?　　　　 （ ´_ゝ`）　/ 　 ⌒i
# ?　　　　／　　　＼ 　 　  |　|
# ? 　　　 / 　　 /￣￣￣￣/　| 　 |
# ?　 ＿_(__ﾆつ / 　    ＿/ . | . |＿＿＿＿
# ?　 　　　＼/＿＿＿＿/　（u　⊃
# ?
# ? /\_ /
# ?		(=._.)
# ? / >WA \> AC
# ?
#       WELCOME TO MY CODING SPACE
# ! Filename: C_Grid_game.py
# * Folder: D: \Code\Python\Codeforces\ProblemSet\Topic Stream Mashup Constructives
# ?      Author: TranDucTri2003
# TODO   CreatedAt: 08/27/2022 11: 41: 49
# ? - ----------------------------------------------------------------------------------------------------
def check(matrix):
    ok = False
    # Ngang
    for i in range(4):
        if matrix[i][0] == 1 and matrix[i][1] == 1 and matrix[i][2] == 1 and matrix[i][3] == 1:
            matrix[i][0] = 0
            matrix[i][1] = 0
            matrix[i][2] = 0
            matrix[i][3] = 0
            ok = True
    # Doc
    for i in range(4):
        if matrix[0][i] == 1 and matrix[1][i] == 1 and matrix[2][i] == 1 and matrix[3][i] == 1:
            matrix[0][i] = 0
            matrix[1][i] = 0
            matrix[2][i] = 0
            matrix[3][i] = 0
            ok = True
    if ok == True:
        return True

    return False


def test(matrix, info):
    if info == 0:  # Doc
        # print("doc")
        for i in range(0, 3):
            for j in range(0, 4):
                if matrix[i][j] == 0 and matrix[i+1][j] == 0:
                    matrix[i][j] = 1
                    matrix[i+1][j] = 1
                    if check(matrix) == True:
                        return i+1, j+1
                    else:
                        matrix[i][j] = 0
                        matrix[i+1][j] = 0

        # print("Free")
        for i in range(0, 3):
            for j in range(0, 4):
                if matrix[i][j] == 0 and matrix[i+1][j] == 0:
                    matrix[i][j] = 1
                    matrix[i+1][j] = 1
                    return i+1, j+1

    else:
        # print('ngang')
        for i in range(0, 4):
            for j in range(0, 3):
                if matrix[i][j] == 0 and matrix[i][j+1] == 0:
                    matrix[i][j] = 1
                    matrix[i][j+1] = 1
                    if check(matrix) == True:
                        return i+1, j+1
                    else:
                        matrix[i][j] = 0
                        matrix[i][j+1] = 0

        # print("free")
        for i in range(0, 4):
            for j in range(0, 3):
                if matrix[i][j] == 0 and matrix[i][j+1] == 0:
                    matrix[i][j] = 1
                    matrix[i][j+1] = 1
                    return i+1, j+1


s = input()
matrix = [[0 for i in range(4)]for i in range(4)]
for i in range(len(s)):
    print(*test(matrix, int(s[i])))
    # for i in range(4):
    #     print(matrix[i])
    # print()


# s = input()

# doc = False
# ngang = False
# for i in range(len(s)):
#     if s[i] == "0":
#         if doc == False:
#             print(3, 1)
#             doc = True
#         else:
#             print(1, 1)
#             doc = False
#     else:
#         if ngang == False:
#             print(1, 3)
#             ngang = True
#         else:
#             print(1, 1)
#             ngang = False
