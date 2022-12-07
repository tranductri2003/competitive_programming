
class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def DFS(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0
                or r >= ROWS or c >= COLS
                or word[i] != board[r][c]
                    or (r, c) in path):
                return False
            path.add((r, c))
            res = (DFS(r+1, c, i+1)
                   or DFS(r-1, c, i+1)
                   or DFS(r, c+1, i+1)
                   or DFS(r, c-1, i+1))
            path.remove((r, c))
            return res
        for i in range(ROWS):
            for j in range(COLS):
                if DFS(i, j, 0):
                    return True
        return False


t = Solution()
(t.exist([["1", "2", "3", "4"], ["5", "6", "7", "8"],
 ["9", "10", "11", "12"]], "123456"))
