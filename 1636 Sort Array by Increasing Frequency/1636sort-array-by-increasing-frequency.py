class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        m=[]
        c=1
        for i in range(n-2,-1,-1):
            if nums[i]==nums[i+1]:c+=1
            else: m.append([nums[i+1],c]);c=1
        m.append([nums[0],c])
        m.sort(key=lambda x: (x[1]))
        ans = []
        for value,count in m:
            for _ in range(count):
                ans.append(value)

        return ans