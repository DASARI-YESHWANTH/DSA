class Solution:
    def reverseList(self, head: Optional['ListNode']) -> Optional['ListNode']:
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # save the next node
            curr.next = prev        # reverse the link
            prev = curr             # move prev forward
            curr = next_node        # move curr forward

        return prev  # new head of the reversed list


        