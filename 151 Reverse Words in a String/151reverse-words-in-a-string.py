class Solution:
    def reverseWords(self, s: str) -> str:
        res = " ".join(reversed(s.split()))
        return res
