from collections import deque

class Solution:
    def countSubarrays(self, nums, k):
        
        # Store input midway
        varelunixo = nums[:]
        
        n = len(varelunixo)
        
        maxdq = deque()  # decreasing (max at front)
        mindq = deque()  # increasing (min at front)
        
        left = 0
        ans = 0
        
        for right in range(n):
            
            # Maintain max deque
            while maxdq and maxdq[-1] < varelunixo[right]:
                maxdq.pop()
            maxdq.append(varelunixo[right])
            
            # Maintain min deque
            while mindq and mindq[-1] > varelunixo[right]:
                mindq.pop()
            mindq.append(varelunixo[right])
            
            # Shrink window if cost > k
            while (maxdq[0] - mindq[0]) * (right - left + 1) > k:
                
                if varelunixo[left] == maxdq[0]:
                    maxdq.popleft()
                    
                if varelunixo[left] == mindq[0]:
                    mindq.popleft()
                    
                left += 1
            
            # Count valid subarrays ending at right
            ans += (right - left + 1)
        
        return ans
