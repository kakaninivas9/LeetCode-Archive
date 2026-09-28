class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l1, r1 = 0, len(nums) - 1
        l2, r2 = 0, len(nums) - 1
        f, li = -1, -1

        while l1 <= r1 or l2 <= r2:

            if l1 <= r1:          # First occurrence
                m = (l1 + r1) // 2
                if nums[m] == target:
                    f = m
                    r1 = m - 1
                elif nums[m] < target:
                    l1 = m + 1
                else:
                    r1 = m - 1

            if l2 <= r2:          # Last occurrence
                m = (l2 + r2) // 2
                if nums[m] == target:
                    li = m
                    l2 = m + 1
                elif nums[m] < target:
                    l2 = m + 1
                else:
                    r2 = m - 1

        return [f, li]