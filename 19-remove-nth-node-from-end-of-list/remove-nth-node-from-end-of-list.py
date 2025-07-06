# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=1
        temp=head
        if head is None or head.next is None:
            return None
        while temp.next is not None:
            temp=temp.next
            c+=1
        if c==n:
            new_head=head.next
            return new_head
        
        temp=head
        k=1
        while k !=c-n:
            
            temp=temp.next
            k+=1
        temp.next=temp.next.next
        return head