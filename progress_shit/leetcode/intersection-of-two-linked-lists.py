# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA=headA
        count1=0
        while currA:
            currA=currA.next
            count1+=1
        
        currB=headB
        count2=0
        while currB:
            currB=currB.next
            count2+=1

        diff=max(count1, count2)- min(count1, count2)
        shift_ptr=None
        if count1>count2:
            shift_ptr=headA
            other_ptr=headB
            for _ in range(diff):
                shift_ptr=shift_ptr.next
            while shift_ptr and other_ptr:
                if shift_ptr==other_ptr:
                    return shift_ptr
                shift_ptr=shift_ptr.next
                other_ptr=other_ptr.next
                
        else:
            shift_ptr=headB
            other_ptr=headA
            for _ in range(diff):
                shift_ptr=shift_ptr.next
            while shift_ptr and other_ptr:
                if shift_ptr==other_ptr:
                    return shift_ptr
                shift_ptr=shift_ptr.next
                other_ptr=other_ptr.next
        return None
        


        

        


