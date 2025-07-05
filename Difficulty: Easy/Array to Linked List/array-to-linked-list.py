class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def constructLL(self, arr):
        head = None
        tail = None
        for val in arr:
            new_node = Node(val)
            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
        return head

        
        