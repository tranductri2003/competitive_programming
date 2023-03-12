# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA = headA
        pB = headB
        while pA != pB:
            if pA:
                pA = pA.next
            else:
                pA = headB

            if pB:
                pB = pB.next
            else:
                pB = headA
        return pA
