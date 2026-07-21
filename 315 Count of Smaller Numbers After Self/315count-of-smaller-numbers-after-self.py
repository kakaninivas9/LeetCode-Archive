class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        rank = {num: i + 1 for i, num in enumerate(sorted({*nums}))}
        m = len(rank)
        tree = [0] * (m + 1)
        res = [0] * n

        for i in range(n - 1, -1, -1):
            r = rank[nums[i]]
            j = r - 1
            s = 0

            while j:
                s += tree[j]
                j -= j & -j

            res[i] = s
            j = r

            while j <= m:
                tree[j] += 1
                j += j & -j

        return res