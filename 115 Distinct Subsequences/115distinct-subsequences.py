#very cool solution
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n: 
            return 0
        if m == n: 
            return 1 if s == t else 0
        dp = [0] * n  + [1]
        #dp of i, j tells me how many ways can i make t[j:] using chars from s[i:], so dp or 0,0 is the answer
        for i in range(m - 1, -1, -1):
            start_j = max(0, n - m + i)
            end_j = min(n - 1, i)
            for j in range(start_j, end_j + 1):
                if s[i] == t[j]:
                    dp[j] += dp[j+1] #since you're populating from the left to the right, the right ones have the old values anyways,from i-1, so it updates properly
        
        return dp[0]