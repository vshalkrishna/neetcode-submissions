# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recur(root):
            if not root:
                return 0
            #root 2
            left = recur(root.left)#1
            right = recur(root.right)#0
            return 1 + max(left, right)#
        return recur(root)

