class Solution(object):
    def isValid(self, num, r, c, board):
        for i in range(9):
            if board[r][i] == str(num) or board[i][c] == str(num) or board[3*(r//3)+i//3][3*(c//3)+i % 3] == str(num):
                return False
        return True

    def solveSudoku(self, board):
        self.solve(board)

    def solve(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for i in range(1, 10):
                        if self.isValid(i, r, c, board):
                            board[r][c] = str(i)
                            if self.solve(board):
                                return True
                            else:
                                board[r][c] = '.'
                    return False
        return True
