from collections import defaultdict
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        level = defaultdict(lambda: -1)
        level[root] = 1
        queue = [root]
        data = []
        maxLevel = 1
        while queue:
            node = queue.pop(0)
            data.append(node)
            if node.left is not None:
                level[node.left] = level[node]+1
                maxLevel = max(maxLevel, level[node]+1)
                queue.append(node.left)
            if node.right is not None:
                level[node.right] = level[node]+1
                maxLevel = max(maxLevel, level[node]+1)
                queue.append(node.right)

        res = []
        for l in range(1, maxLevel+1):
            temp = []
            for node in data:
                if level[node] == l:
                    temp.append(node.val)
            if l % 2 == 0:
                temp = temp[::-1]
            res.append(temp)
        return res


t = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
# root = TreeNode(1)
print(t.zigzagLevelOrder(root))
