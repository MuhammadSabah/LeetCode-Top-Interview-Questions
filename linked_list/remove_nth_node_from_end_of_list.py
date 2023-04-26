# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        node = head
        while node is not None:
            l += 1
            node = node.next

        d = l - n
        m = d + 1
        if d == 0:
            return head.next
        prev_node = None
        curr_node = head

        for i in range(1, m):
            prev_node = curr_node
            curr_node = curr_node.next

        prev_node.next = prev_node.next.next
        return head
