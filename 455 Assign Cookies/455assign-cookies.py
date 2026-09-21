class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        j = 0
        for cookie in s:
            if j == len(g):
                break
            if cookie >= g[j]:
                j += 1

        return j