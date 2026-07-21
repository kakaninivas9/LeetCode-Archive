class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        
        def backtrack(row: int, cols: int, diag1: int, diag2: int):
            # Base case: If all queens are placed successfully
            if row == n:
                self.count += 1
                return
            
            # Form a bitmask of all available positions in the current row
            # 1 represents an available position, 0 represents an attacked position
            available_positions = ((1 << n) - 1) & ~(cols | diag1 | diag2)
            
            while available_positions:
                # Isolate the lowest set bit (the next available position)
                position = available_positions & -available_positions
                
                # Clear this position from the available pool
                available_positions &= available_positions - 1
                
                # Move to the next row with updated tracking masks
                backtrack(
                    row + 1, 
                    cols | position, 
                    (diag1 | position) << 1, 
                    (diag2 | position) >> 1
                )
        
        # Start backtracking from row 0 with empty tracking masks
        backtrack(0, 0, 0, 0)
        return self.count

# Example usage:
# solver = Solution()
# print(solver.totalNQueens(4))  # Output: 2