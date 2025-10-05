# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(val=-1)
        sums = head
        carry = 0

        while l1 or l2:
            new_node = ListNode(val=-1)
            add = 0
            if l1:
                add += l1.val
                l1 = l1.next
            
            if l2:
                add += l2.val
                l2 = l2.next
            
            add += carry
            carry = 0
            if add > 9:
                carry, add = add // 10, add % 10
            
            
            new_node.val = add
            sums.next = new_node
            sums = new_node
        
        if carry:
            sums.next = ListNode(val=carry)
        
        return head.next
