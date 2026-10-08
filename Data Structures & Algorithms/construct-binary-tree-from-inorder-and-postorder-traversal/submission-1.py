# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #Inorder  -> L C R
        #Postorder -> L R C
        dictionary = {val:idx for idx, val in enumerate(inorder)}
        def recur(left, right):
            if left > right:
                return None
            #post order last elemebt is alwayus the root
            root = postorder.pop() if postorder else None
            Root = TreeNode(val = root)
            #Root need to find the idx in inorder
            idx = dictionary[root]
            # print(f"the idx is {idx\}")
            # print(f"the root left{Root.left\}")
            Root.right = recur(idx+1, right)
            # print(f"the root right{Root.right\}")
            Root.left = recur(left, idx-1)


            # print(f"--------------")
            # print(f"the tree build {Root\}")



            return Root
        
        return recur(0, len(inorder)-1)

        




        