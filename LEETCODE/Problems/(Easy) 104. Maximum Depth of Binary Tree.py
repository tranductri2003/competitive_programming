# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def DFS(node, count):
            if not node:
                return
            else:
                self.res = max(self.res, count)
                DFS(node.left, count+1)
                DFS(node.right, count+1)
        self.res = 0
        DFS(root, 1)
        return self.res
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         leftSubtree = self.maxDepth(root.left)
#         RightSubtree = self.maxDepth(root.right)
#         return max(leftSubtree, RightSubtree) + 1
