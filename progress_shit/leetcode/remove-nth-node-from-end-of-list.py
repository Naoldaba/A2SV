# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        cur=head
        while cur:
            cur=cur.next
            count+=1

        print(count)
        ind=1
        cur=head
        if count==1 and n==1:
            return None
        while cur.next:
            if count-n==0:
                head=cur.next
                break
            elif ind == count-n:
                cur.next=cur.next.next
                break
            cur=cur.next
            ind+=1
        return head
        print(count)

        