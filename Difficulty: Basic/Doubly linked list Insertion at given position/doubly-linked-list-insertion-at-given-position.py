# Your task is to complete this function
# function should add a new node after the pth position
# function shouldn't print or return any data

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    #Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        # Code here
        c=0
        new_node=Node(x)
        if head is None:
            head=new_node
        temp=head
        while c != p and temp.next is not None:
            temp=temp.next
            c+=1
        new_node.next=temp.next
        new_node.prev=temp
        
        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node
        
        return head