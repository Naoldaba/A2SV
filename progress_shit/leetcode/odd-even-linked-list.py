# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=[]
        even=[]
        cur=head
        ind=1
        while cur:
            if ind%2==1:
                odd.append(cur.val)
            else:
                even.append(cur.val)
            ind+=1
            cur=cur.next
        if len(odd)>0:
            cur=head=ListNode(odd[0])
            for i in range(1,len(odd)):
                cur.next=ListNode(odd[i])
                cur=cur.next
            for i in range(len(even)):
                cur.next=ListNode(even[i])
                cur=cur.next
            return head
        return None
        