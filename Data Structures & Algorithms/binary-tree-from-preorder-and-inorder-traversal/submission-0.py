# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        dictionary = {val : idx for idx, val in enumerate(inorder)}

        def recur(left, right):
            if left > right:
                return None
            
            root = preorder.pop(0)#val
            Root = TreeNode(root)
            idx = dictionary[root]
            Root.left = recur(left, idx-1)

            Root.right = recur(idx +1, right)
            

            return Root

        
        return recur(0, len(inorder)-1)
        