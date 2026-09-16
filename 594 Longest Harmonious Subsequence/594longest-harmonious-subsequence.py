class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(i, n):
                if nums[j] - nums[i] == 1:
                    ans = max(ans, j - i + 1)
                elif nums[j] - nums[i] > 1:
                    break

        return ans