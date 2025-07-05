# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        # Copy the value from the next node
        node.val = node.next.val
        # Bypass the next node
        node.next = node.next.next
