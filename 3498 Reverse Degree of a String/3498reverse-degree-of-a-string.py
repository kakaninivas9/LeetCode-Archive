class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum(i * (26 - (ord(ch) - ord('a')))
                   for ch, i in zip(s, range(1, len(s) + 1)))