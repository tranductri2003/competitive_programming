# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def DFS(node):
            if not node:
                return
            else:
                left = DFS(node.left)
                right = DFS(node.right)

                temp = node.left
                node.left = node.right
                node.right = temp
        DFS(root)
        return root
