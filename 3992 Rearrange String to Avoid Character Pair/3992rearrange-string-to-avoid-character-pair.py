class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        # Group characters based on whether they match y, x, or neither
        count_y = [c for c in s if c == y]
        count_x = [c for c in s if c == x]
        others  = [c for c in s if c != x and c != y]
        
        # Combine them safely: y's -> others -> x's
        return "".join(count_y + others + count_x)