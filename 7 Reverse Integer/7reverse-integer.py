class Solution:
    def reverse(self, x: int) -> int:
        a=x
        if x<0:
            x=abs(x)
        ans=0
        while x>0:
            ans=ans*10+(x%10)
            x=x//10
        if ans<(-2**31) or ans>((2**31)-1):
            return 0
        if a>=0:
            return ans
        return -ans
            
        