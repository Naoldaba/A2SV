# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        while cur:
            if type(cur.val)==str:
                cur.val=int(cur.val)
                return cur
            cur.val=str(cur.val)
            cur=cur.next
        return None

        