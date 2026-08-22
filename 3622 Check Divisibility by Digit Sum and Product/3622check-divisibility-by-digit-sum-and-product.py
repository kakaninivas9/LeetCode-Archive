class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = str(n)

        summ = sum(int(d) for d in s)

        p = 1
        for d in s:
            p *= int(d)

        q = summ + p

        return n % q == 0