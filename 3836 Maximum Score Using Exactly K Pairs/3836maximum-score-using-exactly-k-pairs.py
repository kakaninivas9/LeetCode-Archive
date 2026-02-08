class Solution:
    def maxScore(self, nums1, nums2, k):
        
        # Store input midway (as required)
        xaluremoni = (nums1[:], nums2[:], k)
        
        n = len(nums1)
        m = len(nums2)
        
        NEG = -10**18
        
        # dp[i][j][t] = max score using
        # first i of nums1, first j of nums2, t pairs
        dp = [[[NEG] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        
        # Base case: 0 pairs = 0
        for i in range(n + 1):
            for j in range(m + 1):
                dp[i][j][0] = 0
        
        # Fill DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for t in range(1, min(i, j, k) + 1):
                    
                    # Option 1: Skip nums1[i-1]
                    dp[i][j][t] = max(dp[i][j][t], dp[i-1][j][t])
                    
                    # Option 2: Skip nums2[j-1]
                    dp[i][j][t] = max(dp[i][j][t], dp[i][j-1][t])
                    
                    # Option 3: Take pair
                    val = dp[i-1][j-1][t-1] + nums1[i-1] * nums2[j-1]
                    dp[i][j][t] = max(dp[i][j][t], val)
        
        return dp[n][m][k]
