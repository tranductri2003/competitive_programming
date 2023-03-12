# class ListNode(object):
def __init__(self, x):
    self.val = x
    self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        n = 0
        while head:
            n += 1
            if n > 10**4:
                return False
            head = head.next
        return True
