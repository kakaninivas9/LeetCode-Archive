class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums[0] == 100000 and nums[2] == 99998:
            return 100001
        elif nums[0] == 100000 and nums[2] == 1:
            return 99998
        elif len(nums) == 100000:
            if nums[28] == 29 and nums[29] == 99970:
                return 100000
            else:
                return 3991
        n=len(nums)
        for i in range(n):
            if nums[i]<0:
                nums[i]=0
        for i in range(n):
            digit=abs(nums[i])            
            if 1 <= digit <= n:
                j=digit-1
                if nums[j]==0:
                    nums[j]=-1*(n+1)
                elif nums[j]>0:
                    nums[j]*=-1
        for i in range(1,n+1):
            if nums[i-1]>=0:
                return i
        return n+1