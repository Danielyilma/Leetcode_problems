# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for lis in lists:
            
            while lis:
                heappush(heap, lis.val)
                lis = lis.next

        dhead = ListNode()
        cur = dhead

        while len(heap) > 0:
            n = heappop(heap)
            node = ListNode(n)
            cur.next = node
            cur = node


        return dhead.next