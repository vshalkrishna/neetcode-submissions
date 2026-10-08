# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recur(root):
            if not root:
                return [True, 0]
            left =recur(root.left)
            right = recur(root.right)

            balanced =  left[0] and right[0] and abs(right[1]-left[1]) <=1#True iof it a case
            return [balanced, 1 + max(left[1], right[1])]
        return recur(root)[0]

