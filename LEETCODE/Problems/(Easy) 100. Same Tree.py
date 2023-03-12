# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def DFS(node, res):
            if not node:
                res.append(-1)
                return
            else:
                res.append(node.val)
                DFS(node.left, res)
                DFS(node.right, res)
        resP = []
        resQ = []
        DFS(p, resP)
        DFS(q, resQ)
        if resP == resQ:
            return True
        else:
            return False


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
            self.isSameTree(p.left, q.left)
