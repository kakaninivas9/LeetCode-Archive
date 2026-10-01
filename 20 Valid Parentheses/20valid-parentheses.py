class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in d:
                if not stack or stack.pop() != d[ch]:
                    return False
            else:
                stack.append(ch)

        return not stack