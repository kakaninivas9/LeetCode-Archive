from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Frequency of each value
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = how many numbers are divisible by d
        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                cnt[d] += freq[multiple]

        # exact[d] = number of pairs whose GCD is exactly d
        exact = [0] * (mx + 1)

        for d in range(mx, 0, -1):
            c = cnt[d]
            exact[d] = c * (c - 1) // 2

            for multiple in range(2 * d, mx + 1, d):
                exact[d] -= exact[multiple]

        # Prefix count of sorted GCD values
        prefix = []
        values = []

        s = 0
        for d in range(1, mx + 1):
            if exact[d]:
                s += exact[d]
                prefix.append(s)
                values.append(d)

        # Answer queries
        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans