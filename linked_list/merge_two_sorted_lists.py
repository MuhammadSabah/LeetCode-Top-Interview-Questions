# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        temp_node = node

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                temp_node.next = list1
                list1 = list1.next

            else:
                temp_node.next = list2
                list2 = list2.next

            temp_node = temp_node.next

        print(node)
        if list1:
            temp_node.next = list1
        elif list2:
            temp_node.next = list2

        return node.next