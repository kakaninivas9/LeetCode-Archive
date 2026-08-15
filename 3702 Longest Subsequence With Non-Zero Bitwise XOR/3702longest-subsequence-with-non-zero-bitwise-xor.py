class Solution:
    def longestSubsequence(self, nums):
        total_xor = 0

        for x in nums:
            total_xor ^= x

        if total_xor != 0:
            return len(nums)

        # Total XOR is 0.
        # If there is a non-zero element, remove it.
        for x in nums:
            if x != 0:
                return len(nums) - 1

        # All elements are zero
        return 0