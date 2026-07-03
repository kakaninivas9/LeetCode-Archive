class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        m = 0

        for i in nums:
            if i:
                c += 1
            else:
                c = 0

            if c > m:
                m = c

        return m