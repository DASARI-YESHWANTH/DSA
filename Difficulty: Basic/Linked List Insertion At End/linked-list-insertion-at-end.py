   
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def insertAtEnd(self, head, x):
        
        new_node= Node(x)
        if head is None:
            return new_node
        curr=head
        while curr.next != None:
            curr=curr.next
        curr.next= new_node
        return head
        