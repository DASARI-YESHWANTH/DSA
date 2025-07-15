class Solution:
    def delete_node(self, head, x):
        #code here
     
        if head is None:
            return None
    
        # If the node to delete is the head (1-based index)
        if x == 1:
            new_head = head.next
            if new_head is not None:
                new_head.prev = None
            return new_head
    
        temp = head
        count = 1
    
        while count < x and temp is not None:
            temp = temp.next
            count += 1
    
        # If the node to delete exists
        if temp is not None:
            if temp.prev is not None:
                temp.prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = temp.prev
    
        return head
