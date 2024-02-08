# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        count=0
        while cur:
            count+=1
            cur=cur.next
        mid=count//2
        print(count)
        ind=0

        cur=head
        while cur:
            if ind==mid:
                head=cur
                break
            ind+=1
            cur=cur.next
        return head