class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def recur(root):
            if not root:
                return 0

            left = recur(root.left)#0
            right = recur(root.right)#0
            self.max_diameter = max(self.max_diameter, left + right)
            print(f"the root node is {root.val}")
            print(f"the length of  left node down from  the parent {root.val} is : {left}")
            print(f"the length of right node down  from the parent :{root.val} is : {right}")
            print(f"the value to the top is {1 + max(left, right)}")
            return 1 + max(left, right)#
        recur(root)
        return self.max_diameter