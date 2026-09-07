class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur = max = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur += nums[i]
            else:
                cur = nums[i]

            if cur > max:
                max = cur

        return max