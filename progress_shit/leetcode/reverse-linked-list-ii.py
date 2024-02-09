# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp=[]
        ind=1
        cur=head
        while cur:
            if left<=ind<=right:
                temp.append(cur.val)
            cur=cur.next
            ind+=1
        pos=1

        cur=head
        while cur:
            if left<=pos<=right:
                cur.val=temp.pop()
            cur=cur.next
            pos+=1

        return head

