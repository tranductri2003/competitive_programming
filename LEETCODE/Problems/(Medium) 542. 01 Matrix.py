class Solution(object):

    # def check(i, j, row, collumn):

    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        height = len(mat)
        width = len(mat[0])

        queue = []
        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = "#"

        for row, collumn in queue:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                X = row+dx
                Y = collumn+dy
                if 0 <= X <= height-1 and 0 <= Y <= width-1 and mat[X][Y] == "#":
                    mat[X][Y] = mat[row][collumn]+1
                    queue.append((X, Y))
        return mat
