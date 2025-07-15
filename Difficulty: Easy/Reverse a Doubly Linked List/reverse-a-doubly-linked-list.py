'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        if head is None:
            return head
        prev=None
        temp=head
        front=temp.next
        while temp is not None and temp.next is not None:
            temp.next=prev
            temp.prev=front
            prev=temp
            temp=front
            front=front.next
        temp.next=prev
        head=temp
        return head