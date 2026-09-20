class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            b=str(nums[i])
            for j in range(len(b)):
                a.append(int(b[j]))
        return a