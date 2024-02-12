# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        cur=head
        while cur:
            arr.append(cur.val)
            cur=cur.next
        for i in range(len(arr)):
            j=i
            while j>0 and arr[j]<arr[j-1]:
                arr[j], arr[j-1]=arr[j-1], arr[j]
                j-=1
        cur=head=ListNode(arr[0])
        for i in range(1,len(arr)):
            cur.next=ListNode(arr[i])
            cur=cur.next
        return head

        
        