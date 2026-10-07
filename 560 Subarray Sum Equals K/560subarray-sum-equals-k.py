class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = Counter({0 : 1})
        cur = 0
        res = 0
        for i in nums:
            cur += i
            if cur - k in count:
                res+= count[cur - k]
            count[cur]+=1
        return res