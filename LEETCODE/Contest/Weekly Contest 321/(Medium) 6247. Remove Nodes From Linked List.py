from collections import Counter
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        data = []
        while head != None:
            data.append(head.val)
            head = head.next

        newData = []
        for num in data:
            newData.append(num)

        mangdasapxep = sorted(data)
        mangdasapxep.insert(0, 0)
        tanso = dict(Counter(mangdasapxep))
        mangdasapxep = list(set(mangdasapxep))
        mangdasapxep = sorted(mangdasapxep)
        pointer = len(mangdasapxep)-1
        currMax = []

        for num in data:
            tanso[num] -= 1
            while tanso[mangdasapxep[pointer]] == 0:
                pointer -= 1
            currMax.append(mangdasapxep[pointer])

        res = []
        for i in range(0, len(newData)):
            if newData[i] >= currMax[i]:
                res.append(newData[i])

        head = None
        curr = None
        for num in res:
            newNode = ListNode(num)
            if head == None:
                head = newNode
                curr = head
            else:
                curr.next = newNode
                curr = curr.next
        return head


# temp = ListNode(5)
# head = temp
# temp = temp.next
# temp.val = 2
# temp = temp.next
# temp.val = 13
# temp = temp.next
# temp.val = 3
# temp = temp.next
# temp.val = 8

# t = Solution()
# print(t.removeNodes(temp))
