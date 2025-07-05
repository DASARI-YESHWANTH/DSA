'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        s=head
        f=head
        while f is not None and f.next is not None:
            s=s.next
            f=f.next.next
            if s==f:
                s=s.next
                count=1
                while s != f:
                    s=s.next
                    count+=1
                return count
        return 0
                    
            