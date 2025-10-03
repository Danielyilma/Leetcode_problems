"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        def sub_flatten(cur_head):

            while cur_head and cur_head.next:
                if cur_head.child:
                    next_val = cur_head.next
                    cur_head.child.prev = cur_head
                    cur_head.next = cur_head.child

                    child_tail = sub_flatten(cur_head.child)
                    cur_head.child = None
                    child_tail.next = next_val
                    next_val.prev = child_tail
                    cur_head = next_val
                else:
                    cur_head = cur_head.next
            
            if cur_head.child:
                child_tail = sub_flatten(cur_head.child)
                cur_head.next = cur_head.child
                cur_head.child.prev = cur_head
                cur_head.child = None
                cur_head = child_tail
            
            return cur_head
        
        sub_flatten(head)
        return head

        