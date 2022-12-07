class Solution:
    def diameterOfBinaryTree(self, root):
        n = len(root)
        root.insert(0, 0)
        res = 0
        i = 2
        while i <= n:
            res += 1
            i *= 2
        i = 3
        while i <= n:
            res += 1
            i *= 2
        print(res)
