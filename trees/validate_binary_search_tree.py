# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid_node(node, left, right):
            if not node:
                return True

            if not (node.val < right and left < node.val):
                return False

            return (valid_node(node.left, left, node.val) and
                    valid_node(node.right, node.val, right))

        return valid_node(root, float("-inf"), float("inf"))