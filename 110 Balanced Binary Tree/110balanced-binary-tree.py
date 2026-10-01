class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0, True
            
            leftHeight, leftBalanced = dfs(root.left)
            rightHeight, rightBalanced = dfs(root.right)

            height = max(leftHeight, rightHeight) + 1
           
            if not leftBalanced or not rightBalanced or abs(leftHeight - rightHeight) > 1:
                return height, False

            return height, True
        
        height, balanced = dfs(root)
        return balanced
