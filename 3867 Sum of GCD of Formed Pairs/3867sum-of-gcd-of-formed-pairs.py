from math import gcd

class Solution:
    def gcdSum(self, A):
        g = gcd
        m = 0
        for i, x in enumerate(A):
            if x > m:
                m = x
            A[i] = g(x, m)
        A.sort()
        return sum(g(A[i], A[~i]) for i in range(len(A)//2))