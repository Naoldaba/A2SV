# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        arr1=[]
        arr2=[]
        cur=head
        while cur:
            if cur.val<x:
                arr1.append(cur.val)
            else:
                arr2.append(cur.val)
            cur=cur.next
        if len(arr1)>0:
            cur=head=ListNode(arr1[0])
            for i in range(1,len(arr1)):
                cur.next=ListNode(arr1[i])
                cur=cur.next
        
            for i in range(len(arr2)):
                cur.next=ListNode(arr2[i])
                cur=cur.next
        return head

        print(arr1, arr2)

        