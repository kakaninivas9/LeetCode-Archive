class Solution:
    def reverseWords(self, s: str) -> str:
        parts = s.split()
        for i in range(len(parts)):
            parts[i]= parts[i][::-1]
        return " ".join(parts)