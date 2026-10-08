# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        stack = deque([root])
        result = []

        while stack:
            level_size = len(stack)

            for i in range(level_size):
                node = stack.popleft()
                
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)

                if i == 0: result.append(node.val)

        return result[-1]

             