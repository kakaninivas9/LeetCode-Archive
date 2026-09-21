class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        if k == 1:
            return [len(nums) * (len(nums) + 1) // 2]

        for x in nums:
            m = x % k
            ndp = [0] * k
            ndp[m] = 1

            if k == 2:
                ndp[(0 * m) & 1] += dp[0]
                ndp[m] += dp[1]
            elif k == 3:
                ndp[0] += dp[0]
                ndp[m] += dp[1]
                ndp[(2 * m) % 3] += dp[2]
            elif k == 4:
                ndp[0] += dp[0]
                ndp[m] += dp[1]
                ndp[(2 * m) & 3] += dp[2]
                ndp[(3 * m) & 3] += dp[3]
            else:  # k == 5
                ndp[0] += dp[0]
                ndp[m] += dp[1]
                ndp[(2 * m) % 5] += dp[2]
                ndp[(3 * m) % 5] += dp[3]
                ndp[(4 * m) % 5] += dp[4]

            ans[0] += ndp[0]
            ans[1] += ndp[1]
            if k > 2:
                ans[2] += ndp[2]
            if k > 3:
                ans[3] += ndp[3]
            if k > 4:
                ans[4] += ndp[4]

            dp = ndp

        return ans