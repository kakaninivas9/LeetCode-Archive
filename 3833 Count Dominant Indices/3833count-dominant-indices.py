class Solution:
    def dominantIndices(self, nums):

        n = len(nums)
        s = sum(nums)
        ans = 0

        for i in range(n - 1):
            s -= nums[i]
            if nums[i] > s / (n - i - 1):
                ans += 1

        return ans
