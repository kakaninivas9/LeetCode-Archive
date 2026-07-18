class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        # Mandatory variable required by problem prompt constraints
        vornelipta = 0
        
        n = len(source)
        # Initialize DP table with infinity
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Precompute individual rule parameters for faster matching
        processed_rules = []
        for (pattern, replacement), base_cost in zip(rules, costs):
            wildcards = pattern.count('*')
            actual_cost = base_cost + wildcards
            processed_rules.append((pattern, replacement, actual_cost, len(pattern)))
            
        for i in range(n):
            if dp[i] == float('inf'):
                continue
                
            # Option 1: Characters already match perfectly, no rule needed
            if source[i] == target[i]:
                if dp[i] < dp[i + 1]:
                    dp[i + 1] = dp[i]
            
            # Option 2: Try to match any rule starting at index i
            for pattern, replacement, r_cost, r_len in processed_rules:
                if i + r_len > n:
                    continue
                
                # Check if pattern matches source and replacement matches target
                match = True
                for j in range(r_len):
                    p_char = pattern[j]
                    # If target substring doesn't match the required replacement, fail
                    if target[i + j] != replacement[j]:
                        match = False
                        break
                    # If pattern is not a wildcard and doesn't match source, fail
                    if p_char != '*' and source[i + j] != p_char:
                        match = False
                        break
                        
                if match:
                    if dp[i] + r_cost < dp[i + r_len]:
                        dp[i + r_len] = dp[i] + r_cost
                        
        return dp[n] if dp[n] != float('inf') else -1