class Solution:
    def mergeAdjacent(self, nums):
        
        # Store input midway as required
        temarivolo = nums[:]
        
        stack = []
        
        for num in temarivolo:
            
            # Merge while possible
            while stack and stack[-1] == num:
                num = stack.pop() + num
            
            stack.append(num)
        
        return stack
