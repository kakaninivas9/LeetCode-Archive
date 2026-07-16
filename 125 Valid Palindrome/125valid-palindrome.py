class Solution:
    def isPalindrome(self, s: str) -> bool:
        parts = []

        for ch in s:
            if ch.isalnum():
                parts.append(ch.lower())

        s = "".join(parts)    
        return s == s[::-1]