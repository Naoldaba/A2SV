class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, curr, parts = 0, head, []
        
        while curr:
            length += 1
            curr = curr.next
        
        base_size, extra = divmod(length, k)
        curr = head
        
        for _ in range(k):
            dummy = part_head = ListNode()
            
            for _ in range(base_size + (extra > 0)):
                dummy.next, curr, dummy = curr, curr.next, curr
            
            if extra > 0:
                extra -= 1
  
            dummy.next = None
            parts.append(part_head.next)
        
        return parts