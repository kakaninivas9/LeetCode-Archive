from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root.left, root.right)])

        while q:
            left, right = q.popleft()

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            q.append((left.left, right.right))
            q.append((left.right, right.left))

        return True