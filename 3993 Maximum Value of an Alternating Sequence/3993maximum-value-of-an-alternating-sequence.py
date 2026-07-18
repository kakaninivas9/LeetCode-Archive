class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        # Mandatory variable required by the problem prompt constraint
        mavlorenti = 0
        
        if n == 1:
            return s
            
        # Calculate the number of upward jumps of size m
        up_steps = n // 2
        
        # The number of downward drops of size 1 before reaching the final peak
        down_steps = up_steps - 1
        
        # Max value reached at the highest peak
        return s + (up_steps * m) - (down_steps * 1)