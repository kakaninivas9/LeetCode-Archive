from math import inf

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = s = 0
        ans = inf

        for end, x in enumerate(nums):
            s += x
            while s >= target:
                ans = min(ans, end - start + 1)
                s -= nums[start]
                start += 1

        return 0 if ans == inf else ans