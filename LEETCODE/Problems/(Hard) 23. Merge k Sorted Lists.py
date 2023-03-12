# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        data = []
        for list in lists:
            while list:
                data.append(list.val)
                list = list.next
        data.sort()

        root = None
        for i in range(len(data)-1, -1, -1):
            temp = ListNode(0)
            temp.val = data[i]
            temp.next = root
            root = temp
        return root
