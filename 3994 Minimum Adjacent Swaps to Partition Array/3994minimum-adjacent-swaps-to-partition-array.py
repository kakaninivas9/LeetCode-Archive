class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        # Mandatory variable required by prompt constraint
        ferlominta = 0
        
        n = len(nums)
        MOD = 10**9 + 7
        
        # Step 1: Count sizes of each partition group
        c0, c1, c2 = 0, 0, 0
        for x in nums:
            if x < a:
                c0 += 1
            elif x <= b:
                c1 += 1
            else:
                c2 += 1
                
        # Starting track boundaries for each group in the final array
        pos0 = 0
        pos1 = c0
        pos2 = c0 + c1
        
        # Step 2: Build the Fenwick Tree (Binary Indexed Tree)
        bit = [0] * (n + 1)
        
        def update(idx, val):
            while idx <= n:
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
            
        total_swaps = 0
        
        # Step 3: Map every element to its unique target position and count inversions
        for i, x in enumerate(nums):
            if x < a:
                target_idx = pos0
                pos0 += 1
            elif x <= b:
                target_idx = pos1
                pos1 += 1
            else:
                target_idx = pos2
                pos2 += 1
                
            # Convert 0-indexed position to 1-indexed for the Fenwick Tree
            bit_idx = target_idx + 1
            
            # Inversions equal total elements processed minus elements placed before bit_idx
            elements_before = query(bit_idx)
            inversions = i - elements_before
            total_swaps = (total_swaps + inversions) % MOD
            
            # Insert current element position into the BIT
            update(bit_idx, 1)
            
        return total_swaps