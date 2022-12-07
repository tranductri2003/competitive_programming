
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1=l1
        num1=[]
        while head1!=None:
            num1.append(head1.val)
            head1=head1.next
        
        head2=l2
        num2=[]
        while head2!=None:
            num2.append(head2.val)
            head2=head2.next

        num1=num1[::-1]
        num2=num2[::-1]
        for i in range(len(num1)):
            num1[i] = str(num1[i])
        for i in range(len(num2)):
            num2[i] = str(num2[i])
                
        num1=int("".join(num1))
        num2=int("".join(num2))

        res=num1+num2
        res=str(res)[::-1]
        res=list(res)
        
        for i in range(len(res)):
            res[i] = int(res[i])
            
        head=None
        for currData in res:
            newNode=ListNode(currData)
            if head==None:
                head=newNode
            else:
                curr=head
                while curr.next!=None:
                    curr=curr.next
                curr.next=newNode
        return head

    