class Solution:
    def isHappy(self, n: int) -> bool:    
        visit = set()
        
        def get_next_number(n):    
            output = 0
            
            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            
            return output

        while n not in visit:
            visit.add(n)
            n = get_next_number(n)
            if n == 1:
                return True
        
        return False
        
# class Solution:
#     def isHappy(self, n: int) -> bool:    
        
#         def get_next_number(n):    
#             output = 0
            
#             while n:
#                 digit = n % 10
#                 output += digit ** 2
#                 n = n // 10
            
#             return output

#         slow = get_next_number(n)
#         fast = get_next_number(get_next_number(n))

#         while slow != fast:
#             if fast == 1: return True
#             slow = get_next_number(slow)
#             fast = get_next_number(get_next_number(fast))

#         return slow == 1