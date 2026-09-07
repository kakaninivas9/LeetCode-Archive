class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        ns = 0
        max = -float('inf')
        start = 0 
        end = 0
        for i in range(n):
            sum += nums[i]
            if sum > max:
                max = sum 
                start = ns
                end = i
            if sum < 0:
                ns = i+1
                sum =0
        return max
            


                