class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        d = {}

        for x, y in reservedSeats:
            if x not in d:
                d[x] = set()
            d[x].add(y)

        rc = 2 * n

        for row in d:
            left = all(x not in d[row] for x in [2,3,4,5])
            middle = all(x not in d[row] for x in [4,5,6,7])
            right = all(x not in d[row] for x in [6,7,8,9])

            if left and right:
                continue
            elif left or middle or right:
                rc -= 1
            else:
                rc -= 2

        return rc