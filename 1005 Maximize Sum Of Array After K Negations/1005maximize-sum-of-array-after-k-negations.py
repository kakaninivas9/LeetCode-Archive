class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()

        i = 0
        while i < len(nums) and k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1

        nums.sort()

        if k % 2 == 1:
            nums[0] = -nums[0]

        return sum(nums)