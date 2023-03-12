# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.data = []

        def DFS(node):
            if node:
                DFS(node.left)
                self.data.append(node.val)
                DFS(node.right)
        DFS(root)
        res = 10**9
        for i in range(1, len(self.data)):
            res = min(res, self.data[i]-self.data[i-1])
        return res
