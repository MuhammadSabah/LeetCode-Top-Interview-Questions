# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        output = []
        node = head
        while node:
            output.append(node.val)
            node = node.next

        if len(output) == 0:
            return ouput

        copy_output = output.copy()
        copy_output.reverse()
        return output == copy_output


