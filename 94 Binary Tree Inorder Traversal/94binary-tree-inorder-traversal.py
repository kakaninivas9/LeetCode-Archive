class Solution:
    def inorderTraversal(self, root):
        stack = []
        ans = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
        
            root = stack.pop()
            ans.append(root.val)
            root = root.right

        return ans