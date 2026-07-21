from itertools import chain

class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        flat = list(chain.from_iterable(grid))
        flat = flat[-k:] + flat[:-k]

        return [flat[i:i+n] for i in range(0, total, n)]